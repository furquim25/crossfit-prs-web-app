from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Item


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': ' ',
        'class': 'block w-full bg-white focus:outline-none focus:shadow-outline border border-gray-300 rounded-md py-3 px-3 block appearance-none leading-normal focus:border-blue-400'
    }))
    
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': ' ',
        'class': 'block w-full bg-white focus:outline-none focus:shadow-outline border border-gray-300 rounded-md py-3 px-3 block appearance-none leading-normal focus:border-blue-400'
    }))

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name' ,'password1', 'password2')
        
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your first name',
        'class': 'w-full py-4 px-4 rounded-xl'
    }))
        
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username',
        'class': 'w-full py-4 px-4 rounded-xl'
    }))
    
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Your email',
        'class': 'w-full py-4 px-4 rounded-xl'
    }))
    
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password',
        'class': 'w-full py-4 px-4 rounded-xl'
    }))
    
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
    'placeholder': 'Repeat password',
    'class': 'w-full py-4 px-4 rounded-xl'
    }))

INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'

class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = {'name', 'observation', 'personal_record', 'pr_date'}
        
        widgets = {
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'observation': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            }),
            'personal_record': forms.NumberInput(attrs={
                'class': INPUT_CLASSES
            }),
            'pr_date': forms.DateInput(format=('%Y-%m-%d'), attrs={
                'class': INPUT_CLASSES,
                'type': 'date'
            }),
        }
        
    field_order  = ['name', 'personal_record', 'pr_date', 'observation']

class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = {'name', 'observation', 'personal_record', 'pr_date'}
        
        widgets = {
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'observation': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            }),
            'personal_record': forms.NumberInput(attrs={
                'class': INPUT_CLASSES
            }),
            'pr_date': forms.DateInput(format=('%Y-%m-%d'), attrs={
                'class': INPUT_CLASSES,
                'type': 'date'
            }),
        }
        
    field_order  = ['name', 'personal_record', 'pr_date', 'observation']