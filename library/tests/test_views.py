from django.test import TestCase
from library_app.models import Genre, Author, Book
from django.urls import reverse
from rest_framework.status import HTTP_200_OK as OK
from django.contrib.auth.models import User
from django.test.client import Client


def test_view(url, page_name, template, cls_model=None, attrs=None):
    class ViewTest(TestCase):
        def setUp(self):
            self.client = Client()
            username = password = 'test'
            self.user = User.objects.create_user(username=username, email='a@a.com', password=password)
            self.client.login(username=username, password=password)
            if cls_model:
                for _ in range(100):
                    cls_model.objects.create(**attrs)
        
        def test_exists_by_url(self):
            self.assertEqual(self.client.get(url).status_code, OK)

        def test_exists_by_name(self):
            self.assertEqual(self.client.get(reverse(page_name)).status_code, OK)

        def test_view_template(self):
            response = self.client.get(url)
            self.assertEqual(response.status_code, OK)
            self.assertTemplateUsed(response, template)

    return ViewTest

genre_attrs = {'name': 'genre'}
GenreListViewTest = test_view('/genres/', 'genres', 'catalog/genres.html', Genre, genre_attrs)
author_attrs = {'full_name': 'Fool Name'}
AuthorListViewTest = test_view('/authors/', 'authors', 'catalog/authors.html', Author, author_attrs)
book_attrs = {'title': 'Title'}
BookListViewTest = test_view('/books/', 'books', 'catalog/books.html', Book, book_attrs)
HomePageTest = test_view('', 'homepage', 'index.html')
WeatherPageTest = test_view('/weather/', 'weather', 'pages/weather.html')
