from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    nama = forms.CharField(label="Nama :")
    feedbackUser = forms.CharField(widget=forms.Textarea, label='Feedback :')
    class Meta:
        model = Feedback
        fields = '__all__'