from django.db import models
from uuid import uuid4
from django.core.exceptions import ValidationError
from datetime import datetime


class UUIDMixin(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid4)

    class Meta:
        abstract = True

class CreatedMixin(models.Model):
    created = models.DateTimeField(blank=True, null=True)

    class Meta:
        abstract = True

class ModifiedMixin(models.Model):
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        abstract = True

class Author(UUIDMixin, CreatedMixin, ModifiedMixin):
    full_name = models.CharField(max_length=40)
    books = models.ManyToManyField('Book', through='BookAuthor')

    def __str__(self):
        return self.full_name

    class Meta:
        db_table = 'author'

def positive_int(num: int):
    if num <= 0:
        raise ValidationError(
            f'Value {num} is less or equal zero',
            params={'value': num}
        )

def year_validator(year: int):
    current_year = datetime.now().year
    if year > current_year:
        raise ValidationError(
            f'The year field must be less or equal {current_year}',
            params={'year': year}
        )

book_types = (
    ('book', 'book'),
    ('journal', 'journal')
)

class Book(UUIDMixin, CreatedMixin, ModifiedMixin):
    title = models.CharField(max_length=40)
    description = models.TextField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True, validators=[positive_int])
    age_limit = models.IntegerField(blank=True, null=True, validators=[positive_int])
    year = models.IntegerField(blank=True, null=True, validators=[year_validator])
    type = models.CharField(max_length=20, choices=book_types, blank=False, null=False)
    authors = models.ManyToManyField(Author, through='BookAuthor')
    genres = models.ManyToManyField('Genre', through='BookGenre')

    def __str__(self):
        return f'{self.title}, {self.type}, {self.year}'

    class Meta:
        db_table = 'book'


class BookAuthor(UUIDMixin, CreatedMixin):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    class Meta:
        db_table = 'book_author'
        unique_together = (('book', 'author'),)


class Genre(UUIDMixin, CreatedMixin, ModifiedMixin):
    name = models.CharField(max_length=30)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'genre'

class BookGenre(UUIDMixin, CreatedMixin):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    class Meta:
        db_table = 'book_genre'
        unique_together = (('book', 'genre'),)

