from django import forms
from .models import *


class UpdateTask(forms.ModelForm):
    class Meta():
        model = Tasks
        fields = ('Task_name', 'Description',) 

class CreateTask(forms.ModelForm):
    class Meta():
        model = Tasks
        fields = ('Task_name', 'Description',) 