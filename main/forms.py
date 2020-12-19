from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class FeedbackForm(forms.ModelForm):
    nama = forms.CharField(label="Nama :")
    feedbackUser = forms.CharField(widget=forms.Textarea, label='Feedback :')
    class Meta:
        model = Feedback
        fields = '__all__'
    
class SignUpForm(UserCreationForm):
    password1 = forms.CharField(
        label="Password :",
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'type' : 'password',
                'placeholder': 'Enter your password',
                'name': 'password',
            }
        )
    )
    password2 = forms.CharField(
        label="Password Confirmation :",
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'type' : 'password',
                'placeholder': 'Confirm your password',
                'name': 'password',
            }
        )
    )
    class Meta :
        model = User
        fields= ("email",'username')
        labels ={'username':'Username :','email':'Email :',}
        widgets ={
            'username': forms.TextInput(attrs={'class':'form-control','placeholder': "Enter your username here",  "autocomplete":"off"}),
            'email': forms.TextInput(attrs={'class':'form-control','placeholder': "Enter your email here",  "autocomplete":"off"}),
        }
        help_texts = {
            "username":None,
        }


    
    
    
    

class PenggunaForm(forms.ModelForm):
    class Meta :
        model = Pengguna
        fields =['namalengkap','lokasi','institusi','pekerjaan']
        labels = {'lokasi':'Lokasi :','institusi':'Institusi :','pekerjaan':'Pekerjaan :','namalengkap':"Nama Lengkap :"}
        widgets ={
            'lokasi': forms.TextInput(attrs={'class':'form-control','placeholder': "Enter your location here"}),
            'institusi': forms.TextInput(attrs={'class':'form-control','placeholder': "Enter your Instution here"}),
            'pekerjaan': forms.TextInput(attrs={'class':'form-control','placeholder': "Enter your Work here"}),
            'namalengkap': forms.TextInput(attrs={'class':'form-control','placeholder': "Enter your Full Name here"})}


class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", 
    widget=forms.TextInput(
        attrs={
        'class' : 'form-control',
        'placeholder' : 'Username',
        'type' : 'text',
        'name': 'username',
    }))

    password = forms.CharField(label="Password", 
    widget=forms.PasswordInput(
        attrs={
        'class' : 'form-control',
        'placeholder' : 'Password',
        'type' : 'password',
        'name': 'password',
    }))
