from .models import Donasi
from django import forms

class DonasiForm(forms.ModelForm):
    class Meta:
        model = Donasi
        fields = ('donatur', 'jenis', 'total')
        widgets = {
            'total': forms.TextInput(attrs={"class":"form-control"}),
            
        }