"""
This module defines the URL routes for the 'notes' application.

It includes routes for listing all notes, viewing the details of a
specific note, creating a new note, updating an existing note, and
deleting a note.
"""

from django.urls import path
from .views import (
    NoteListView,
    NoteDetailView,
    NoteCreateView,
    NoteUpdateView,
    NoteDeleteView
)

app_name = 'notes'

urlpatterns = [
    path('', NoteListView.as_view(), name='note_list'),
    path('note/<int:pk>/', NoteDetailView.as_view(), name='note_detail'),
    path('note/new/', NoteCreateView.as_view(), name='note_create'),
    path('note/<int:pk>/edit/', NoteUpdateView.as_view(), name='note_update'),
    path(
        'note/<int:pk>/delete/', NoteDeleteView.as_view(),
        name='note_delete'
    ),
]
