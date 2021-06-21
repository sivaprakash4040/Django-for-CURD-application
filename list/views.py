from list.forms import studentform
from django.forms.forms import Form
from django.shortcuts import render ,redirect
from list.models import student
from list.forms import studentform

# Create your views here.
def display(request):
    s=student.objects.all()
   
    return render(request,'list/home.html',{'s':s})

def creat(request):
    
    if request.method=="POST":
        sno=request.POST['snu']
        sn=request.POST['sn']
        sm=request.POST['sm']
        insert=student(sno=sno,sname=sn,mark=sm)
      
        insert.save()
        return redirect('/home')
       
        
        
   
    return render(request,'list/creat.html')    

def delete(request,id):
        s=student.objects.get(id=id)
        s.delete()
        return redirect('/home')

def update(request,id): 
      s=student.objects.get(id=id)
      if request.method=="POST":
        s.sno=request.POST['snu']
        s.sname=request.POST['sname']
        s.mark=request.POST['smark']
        s.save()
      
        
        return redirect('/home')
       
    
        
        
   
    
      return render(request,'list/update.html',{'s':s})    
