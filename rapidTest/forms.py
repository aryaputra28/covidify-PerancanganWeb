from django import forms
from .models import Rapid
from functools import partial

DateInput = partial(forms.DateInput, {'class': 'datepicker'})

class FormRapid(forms.ModelForm):
    class Meta:
        model = Rapid
        fields = [
            'nama_tempat', 
            'tanggal_pelaksanaan_mulai', 
            'tanggal_pelaksanaan_akhir',
            'biaya', 
            'alamat', 
        ] 
            
    nama_tempat = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Ex: RS Kasih Ibu'}))
    tanggal_pelaksanaan_mulai = forms.DateField(widget=DateInput())
    tanggal_pelaksanaan_akhir = forms.DateField(widget=DateInput())
    biaya = forms.DecimalField(min_value=0, widget=forms.NumberInput(attrs={'placeholder': 'Max: 999.999'}))  