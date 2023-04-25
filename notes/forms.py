from django import forms
from django.core.exceptions import ValidationError

from .models import Notes

class NoteForm(forms.ModelForm):
    class Meta:
        model = Notes

        fields  = ('title', 'text', 'file')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the title here...'}),
            'text': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter the description here...', 'rows': 5}),
            # 'file': forms.FileInput(attrs={'class': 'form-control my-5', 'placeholder': 'Enter the file here...'}),
        }
    
    
