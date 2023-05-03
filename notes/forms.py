from django.core.exceptions import ValidationError
from django import forms
from .models import Notes

class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ('title', 'text')
        labels = {
            'text':'write your thoughts'
        },
        widgets={
            'title': forms.TextInput(attrs={'class':'form-control my-2'}),
            'text': forms.Textarea(attrs={'class': 'form-control my-3'})
        }
    
    def clean_title(self):
        title = self.cleaned_data['title']
        if 'Django' not in title:
            raise ValidationError('We only accept notes about Django!')
        return title