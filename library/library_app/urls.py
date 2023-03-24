from django.urls import path
from .views import custom_main
from .views import BookListView, AuthorListView, GenreListView, book_view, genre_view, author_view


urlpatterns = [
    path('homepage/', custom_main, name='homepage'),
    path('books/', BookListView.as_view(), name='books'),
    path('authors/', AuthorListView.as_view(), name='authors'),
    path('genres', GenreListView.as_view(), name='genres'),
    path('book/', book_view, name='book'),
    path('genre/', genre_view, name='genre'),
    path('author/', author_view, name='author'),
]