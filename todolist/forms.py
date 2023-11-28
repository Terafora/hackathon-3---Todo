from django import forms
from djrichtextfield.widgets import RichTextWidget
from .models import Note

class NoteForm(forms.ModelForm):
    """Form to add a note"""
    title = forms.CharField(label='Title')

    class Meta:
        model = Note
        fields = ['title', 'note']

        widgets = {
            "note": forms.Textarea(attrs={'rows': 5}),
        }

        labels = {
            'note': 'Note',
        }
