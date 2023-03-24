from django.urls import path
from .views import custom_main
from .views import BookListView, AuthorListView, GenreListView


urlpatterns = [
    path('homepage/', custom_main, name='homepage'),
    path('books/', BookListView.as_view(), name='books'),
    path('authors/', AuthorListView.as_view(), name='authors'),
    path('genres', GenreListView.as_view(), name='genres'),
]