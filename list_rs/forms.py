from django import forms
from .models import Rumah_Sakit

class Form_RS(forms.Form):
    provinsi = forms.CharField(label = "Nama Provinsi", 
                                max_length = 100, 
                                widget = forms.TextInput(attrs={
                                "placeholder": "Ex : DKI Jakarta", 
                                "class":"form-control",}))

    nama_rs = forms.CharField(label = "Nama Rumah Sakit", 
                                max_length = 100, 
                                widget = forms.TextInput(attrs={
                                "placeholder": "Ex : RSPI Prof. Dr. Sulianti Saroso", 
                                "class":"form-control",}))

    alamat = forms.CharField(label = "Alamat Rumah Sakit", 
                                max_length = 1000, 
                                widget = forms.TextInput(attrs={ 
                                "class":"form-control",}))

    telepon = forms.IntegerField(label = "No. Telepon Rumah Sakit",  
                                widget = forms.NumberInput(attrs={
                                "placeholder": "Ex : 021-6506559", 
                                "class":"form-control",
                                }))

    website = forms.CharField(label = "Website Rumah Sakit", 
                                max_length = 1000, 
                                widget = forms.TextInput(attrs={
                                "placeholder": "Ex : https://rspi-suliantisaroso.com/", 
                                "class":"form-control",}))
    
    