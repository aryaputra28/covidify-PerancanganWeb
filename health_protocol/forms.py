from django import forms
from .models import Alternative

class AlternativeForm(forms.Form):
    
    text = forms.CharField(label="Apa rekomendasi kamu?",
                                max_length=400,
                                widget=forms.Textarea(attrs={
                                    "placeholder":"Ketik di sini...",
                                    "class":"form-control",
                                    "cols":140,
                                    "rows":10,
                                }))