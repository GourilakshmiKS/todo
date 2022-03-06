from django import forms
from .models import *
from django.forms import ModelForm

class AddListForm(ModelForm):
    class Meta:
        model=List
        fields=['item']