from django import forms
from .models import Document

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('nama', 'jenis', 'total', 'deskripsi', 'document')
        widgets = {
            'nama': forms.TextInput(attrs={"class":"form-control"}),
            'deskripsi': forms.Textarea(attrs={"class":"form-control"}),
            'total': forms.TextInput(attrs={"class":"form-control"}),
        }