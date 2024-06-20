"""
This module contains views for the Note app. It includes views for listing,
detail view, creating, updating, and deleting notes.
"""

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.urls import reverse_lazy
from .models import Note
from .forms import NoteForm


class NoteListView(ListView):
    """
    This view lists all the notes.
    """
    model = Note
    template_name = 'notes/note_list.html'


class NoteDetailView(DetailView):
    """
    This view shows the details of a specific note.
    """
    model = Note
    template_name = 'notes/note_detail.html'


class NoteCreateView(CreateView):
    """
    This view is for creating a new note.
    """
    model = Note
    form_class = NoteForm
    template_name = 'notes/note_form.html'
    success_url = reverse_lazy('notes:note_list')
    success_message = "Note created successfully!"


class NoteUpdateView(UpdateView):
    """
    This view is for updating an existing note.
    """
    model = Note
    form_class = NoteForm
    template_name = 'notes/note_form.html'
    success_url = reverse_lazy('notes:note_list')
    success_message = "Note updated successfully!"


class NoteDeleteView(DeleteView):
    """
    This view is for deleting an existing note.
    """
    model = Note
    template_name = 'notes/note_confirm_delete.html'
    success_url = reverse_lazy('notes:note_list')
    success_message = "Note deleted successfully!"
