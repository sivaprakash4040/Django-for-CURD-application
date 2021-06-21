from django import forms
from django.db import models
from list.models import student

class studentform(forms.ModelForm):
    class Meta:
        model=student
        fields='__all__'