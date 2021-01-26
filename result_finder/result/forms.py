from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
from django import forms
from result.models import *

class CreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class Addstate(forms.ModelForm):
    class Meta:
        model = State
        fields = '__all__'

class Addboard(forms.ModelForm):
    class Meta:
        model = Board
        fields = '__all__'

class Addcourse(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'

class Addstudentdetail(forms.ModelForm):
    class Meta:
        model = Student_detail
        fields = '__all__'