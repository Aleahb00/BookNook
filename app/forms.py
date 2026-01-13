from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.contrib.auth.models import User


class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30,label='First Name', required=True)
    last_name = forms.CharField(max_length=30,label='Last Name')
    username = forms.CharField(max_length=35,label="Username", required=True)
    email = forms.EmailField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'username', 'email','password1', 'password2')


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'pages', 'category', 'bookshelves']
        
class BookshelfForm(forms.ModelForm):
    class Meta:
        model = Bookshelf
        fields = ['name']