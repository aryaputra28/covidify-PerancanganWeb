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
    ""

class LoginForm(AuthenticationForm):
    ""