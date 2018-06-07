from django import forms
from .models import Donatur


class DonaturForm(forms.ModelForm):
    class Meta:
        model = Donatur
        fields = ('nama', 'email', 'alamat', 'contact', 'umur', 'pekerjaan', 'institusi')
        widgets = {
            'nama': forms.TextInput(attrs={"class":"form-control"}),
            'email': forms.TextInput(attrs={"class":"form-control"}),
            'alamat': forms.Textarea(attrs={"class":"form-control"}),
            'contact': forms.TextInput(attrs={"class":"form-control"}),
            'umur': forms.TextInput(attrs={"class":"form-control"}),
            'pekerjaan': forms.TextInput(attrs={"class":"form-control"}),
            'institusi': forms.TextInput(attrs={"class":"form-control"}),
        }


