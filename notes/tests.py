from django.test import TestCase
from django.urls import reverse
from .models import Note


class NoteTests(TestCase):
    def setUp(self):
        self.note = Note.objects.create(title="Тестовая заметка", body="Текст заметки")

    def test_notes_list_view(self):
        response = self.client.get(reverse("notes_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Тестовая заметка")

    def test_note_detail_view(self):
        response = self.client.get(reverse("note_detail", args=[self.note.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Тестовая заметка")
        self.assertContains(response, "Текст заметки")

    def test_note_create_view(self):
        response = self.client.post(
            reverse("note_create"),
            {"title": "Новая заметка", "body": "Содержимое новой заметки"},
        )
        self.assertRedirects(response, reverse("notes_list"))
        self.assertTrue(Note.objects.filter(title="Новая заметка").exists())

    def test_note_edit_view(self):
        response = self.client.post(
            reverse("note_edit", args=[self.note.id]),
            {"title": "Измененный заголовок", "body": "Измененный текст"},
        )
        self.assertRedirects(response, reverse("note_detail", args=[self.note.id]))
        self.note.refresh_from_db()
        self.assertEqual(self.note.title, "Измененный заголовок")

