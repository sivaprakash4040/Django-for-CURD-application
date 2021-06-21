from django.contrib import admin
from list.models import student

# Register your models here.
class studentadmin(admin.ModelAdmin):
    student_list=['sno','sname','smark']
admin.site.register(student,studentadmin)    
