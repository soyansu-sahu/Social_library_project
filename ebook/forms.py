from django import forms
from .models import EBooksModel
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User




class UploadBookForm(forms.ModelForm):
    class Meta:
        model = EBooksModel
        fields = "__all__"



class SignUpForm(UserCreationForm):
    password2 = forms.CharField(label='Confirm Password (again)', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {'email': 'Email'}
