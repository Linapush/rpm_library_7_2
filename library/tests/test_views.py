from django.test import TestCase
from library_app.models import Genre, Author, Book
from django.urls import reverse
from rest_framework.status import HTTP_200_OK as OK


def test_listview(cls_model, url, page_name, template, attrs):
    class ListViewTest(TestCase):
        def setUp(self):
            for _ in range(100):
                cls_model.objects.create(**attrs)
        
        def test_exists_by_url(self):
            assert self.client.get(url).status_code == OK

        def test_exists_by_name(self):
            assert self.client.get(reverse(page_name)).status_code == OK

        def test_view_template(self):
            response = self.client.get(url)
            self.assertEqual(response.status_code, OK)
            self.assertTemplateUsed(response, template)

    return ListViewTest

genre_attrs = {'name': 'genre'}
GenreListViewTest = test_listview(Genre, '/genres/', 'genres', 'catalog/genres.html', genre_attrs)
author_attrs = {'full_name': 'Fool Name'}
AuthorListViewTest = test_listview(Author, '/authors/', 'authors', 'catalog/authors.html', author_attrs)
book_attrs = {'title': 'Title'}
BookListViewTest = test_listview(Book, '/books/', 'books', 'catalog/books.html', book_attrs)
