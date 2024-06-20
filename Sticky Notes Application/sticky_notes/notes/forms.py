"""
This module defines the form for creating and updating notes in the Django
application.

It uses Django's ModelForm, a helper class that lets you create a Form class
from a Django model.
"""

from django import forms
from .models import Note


class NoteForm(forms.ModelForm):
    """
    This class represents a form for creating and updating notes.

    It's a ModelForm associated with the Note model, with fields for the note's
    title and content.
    """

    class Meta:
        model = Note
        fields = ['title', 'content']
