from django import forms
from .models import Alternatives

class AlternativesForm(forms.Form):
    # model = Alternatives
    # fields = ['username', 'text',]
    # labels = {'username':'', 'text':''}
    # widgets = {
    #     'username': forms.TextInput(attrs={'class':'form-control','placeholder': "Put your name here"}),
    #     'text': forms.Textarea(attrs={'class':'form-control','cols': 140,'rows': 10, 'placeholder': "Apa cara lain yang kamu tahu?"})
    # }
    username = forms.CharField(label="Nama",
                                max_length=100,
                                widget=forms.TextInput(attrs={
                                    "placeholder":"",
                                    "class":"form-control",
                                }))
    
    text = forms.CharField(label="Apa rekomendasi kamu?",
                                max_length=400,
                                widget=forms.Textarea(attrs={
                                    "placeholder":"Ketik di sini...",
                                    "class":"form-control",
                                    "cols":140,
                                    "rows":10,
                                }))