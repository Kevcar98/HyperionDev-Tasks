from django.test import TestCase
from .models import Note
from datetime import datetime


class NoteModelTest(TestCase):
    """
    Test case for the Note model.
    """

    def setUp(self):
        """
        This method is run before each test.
        It creates a new Note instance that is used in the tests.
        """
        self.note = Note.objects.create(
            title='Test Note',
            content='This is a test note.'
        )

    def test_note_creation(self):
        """
        This test checks that the note was correctly created by checking it
        title and content.  It also checks that the created_at and updated_at
        fields are instances of datetime.
        """
        self.assertEqual(self.note.title, 'Test Note')
        self.assertEqual(self.note.content, 'This is a test note.')
        self.assertIsInstance(self.note.created_at, datetime)
        self.assertIsInstance(self.note.updated_at, datetime)


class NoteViewTest(TestCase):
    """
    Test case for testing the views related to the Note model.
    """

    def setUp(self):
        """
        This method is run before each test.
        It creates a new Note instance that is used in the tests.
        """
        self.note = Note.objects.create(
            title='Test Note',
            content='This is a test note.'
        )

    def test_note_list_view(self):
        """
        This test checks that the note list view returns a 200 status code
        (indicating success) and that the response contains the title of the
        note created in setUp.
        """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Note')

    def test_note_detail_view(self):
        """
        This test checks that the note detail view for the specific note
        created in setUp returns a 200 status code and that the response
        contains the title of the note.
        """
        response = self.client.get(f'/note/{self.note.pk}/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Note')

    def test_note_create_view(self):
        """
        This test checks that a POST request to the note creation view with
        valid data returns a 302 status code (indicating a redirect, which
        is common after a successful form submission in Django).  It also
        checks that the new note was correctly created by retrieving it
        from the database and checking its content.
        """
        response = self.client.post('/note/new/', {
            'title': 'New Note',
            'content': 'This is a new note.'
        })
        self.assertEqual(response.status_code, 302)
        new_note = Note.objects.get(title='New Note')
        self.assertEqual(new_note.content, 'This is a new note.')

    def test_note_update_view(self):
        """
        This test checks that a POST request to the note update view with valid
        data returns a 302 status code and that the note was correctly updated.
        It does this by refreshing the note from the database and checking its
        title and content.
        """
        response = self.client.post(f'/note/{self.note.pk}/edit/', {
            'title': 'Updated Note',
            'content': 'This is an updated note.'
        })
        self.assertEqual(response.status_code, 302)
        self.note.refresh_from_db()
        self.assertEqual(self.note.title, 'Updated Note')
        self.assertEqual(self.note.content, 'This is an updated note.')

    def test_note_delete_view(self):
        """
        This test checks that a POST request to the note delete view
        returns a 302 status code (indicating a redirect, which is common after
        a successful form submission in Django).  It also checks that the note
        was correctly deleted by checking that it no longer exists in the
        database.
        """
        response = self.client.post(f'/note/{self.note.pk}/delete/')
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Note.objects.filter(pk=self.note.pk).exists())
