from django.contrib import admin
from .models import Book, Genre, Author, BookAuthor, BookGenre
from datetime import datetime


class BookAuthor_inline(admin.TabularInline):
    model = BookAuthor
    extra = 1

class BookGenre_inline(admin.TabularInline):
    model = BookGenre
    extra = 1

class RecencyBookFilter(admin.SimpleListFilter):
    title='recency'
    parameter_name='recency'

    def lookups(self, *_):
        return (
            ('10yo', 'Written in the last 10 years'),
            ('20yo', 'Written in the last 20 years'),
        )
    
    def queryset(self, _, queryset):
        def filter(queryset, year):
            return queryset.filter(year__gte = year)
        if self.value() == '10yo':
            return filter(queryset, datetime.now().year - 10)
        elif self.value() == '20yo':
            return filter(queryset, datetime.now().year - 20)
        return queryset

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    model = Book
    inlines = (BookAuthor_inline, BookGenre_inline)
    list_filter = (
        'genres',
        'type',
        RecencyBookFilter,
        'authors'
    )

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    model = Author
    inlines = (BookAuthor_inline,)

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    model = Genre