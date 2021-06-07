from django.test import TestCase
from django.utils import timezone

from .models import Notes, Category


class NoteTest(TestCase):
    def setUp(self):
        cate = Category.objects.create(name="general")
        self.notes = Notes.objects.create(
            title="Technology",
            content="New tech piece",
            created=timezone.now().strftime("%Y-%m-%d"),
            due_date=timezone.now().strftime("%Y-%m-%d"),
            category=cate,
        )

    def test_get_note(self):
        new_note = self.notes
        self.assertTrue(isinstance(new_note, Notes))
