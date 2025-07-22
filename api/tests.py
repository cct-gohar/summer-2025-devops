from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Book
from django.urls import reverse


class BookAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.book_data = {
            "title": "Clean Code",
            "author": "Robert C. Martin",
            "isbn": "9780132350884",
            "published_date": "2008-08-01",
        }
        self.book = Book.objects.create(**self.book_data)

    def test_create_book(self):
        new_book = {
            "title": "The Pragmatic Programmer",
            "author": "Andrew Hunt",
            "isbn": "9780201616224",
            "published_date": "1999-10-30",
        }
        response = self.client.post("/api/books/", new_book, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["title"], new_book["title"])

    def test_get_book_list(self):
        response = self.client.get("/api/books/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_update_book(self):
        response = self.client.patch(
            f"/api/books/{self.book.id}/", {"title": "Clean Code Updated"}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Clean Code Updated")

    def test_delete_book(self):
        response = self.client.delete(f"/api/books/{self.book.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(id=self.book.id).exists())
