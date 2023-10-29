from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Task

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=False)
    class Meta:
        model= User
        fields= ['username','password1','password2']

class Postform(forms.ModelForm):
    class Meta:
        model=Task
        fields=['text','image','description']

class Updateform(forms.ModelForm):
    class Meta:
        model = Task
        fields=['text','image','description','done']
