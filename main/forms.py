from django import forms
from .models import Feedback
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class FeedbackForm(forms.ModelForm):
    nama = forms.CharField(label="Nama :")
    feedbackUser = forms.CharField(widget=forms.Textarea, label='Feedback :')
    class Meta:
        model = Feedback
        fields = '__all__'
    
class SignUpForm(UserCreationForm):
    username = forms.CharField(
        label="Username",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type' : 'text',
                'placeholder': 'Enter your username',
                'name': 'username',
            }
        ),
        max_length=16
    )

    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'type' : 'email',
                'placeholder': 'Enter your email',
                'name': 'email',
            }
        )
    )

    password1 = forms.CharField(
        label="Password",
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
        label="Password Confirmation",
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'type' : 'password',
                'placeholder': 'Confirm your password',
                'name': 'password',
            }
        )
    )

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
