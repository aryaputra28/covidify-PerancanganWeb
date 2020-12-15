
from django import forms
from .models import *

class pertanyaanForm(forms.ModelForm):
    class Meta :
        model = pertanyaan
        fields =[

            'penanya','location','pertanyaan'
        ]
        labels = {'penanya':'From ','pertanyaan':'Pertanyaan :','location':'Location :'}
        widgets ={
            'penanya': forms.TextInput(attrs={'class':'form-control','placeholder': "Put your name here"}),
            'location': forms.TextInput(attrs={'class':'form-control','placeholder': "Put your location here"}),
            'pertanyaan': forms.Textarea(attrs={'class':'form-control','cols': 140,'rows': 10, 'placeholder': "Put your answer here"})
            }

class komenForm(forms.ModelForm):
    class Meta :
        model = komentar
        fields =['pengomentar','location','komen']
        labels = {'pengomentar':'From :','komen':'Balasan :','location':'Location :'}
        widgets ={
            'pengomentar': forms.TextInput(attrs={'class':'form-control','placeholder': "Put your name here",  "autocomplete":"off"}),
            'location': forms.TextInput(attrs={'class':'form-control','placeholder': "Put your location here"}),
            'komen': forms.Textarea(attrs={'class':'form-control','cols': 10,'rows': 10, 'placeholder': "Put your answer here",  "autocomplete":"off"}), 
            }