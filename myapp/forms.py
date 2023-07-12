from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from myapp.models import BookStore

class SignUpForm(UserCreationForm):
    class Meta:
        model=User
        fields=["first_name","last_name","email","username","password1","password2"]

class SignInForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))

class BooksForm(forms.ModelForm):
    class Meta:
        model=BookStore
        fields=["book_name","price","author","pic","description"]
        widgets={
            "book_name":forms.TextInput(attrs={"class":"form-control"}),
            "price":forms.NumberInput(attrs={"class":"form-control"}),
            "author":forms.TextInput(attrs={"class":"form-control"}),
            "pic":forms.FileInput(attrs={"class":"form-control"}),
            "description":forms.TextInput(attrs={"class":"form-control"})

        }