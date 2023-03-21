from django.contrib import admin
from .models import Book, Genre, Author

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    model = Book

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    model = Genre

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    model = Author