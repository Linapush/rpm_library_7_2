from django.db import models
from uuid import uuid4

class UUIDMixin(models.Model):
    id = models.UUIDField(primary_key=True, defaul=uuid4)

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
    full_name = models.TextField()

    class Meta:
        db_table = 'author'


class Book(UUIDMixin, CreatedMixin, ModifiedMixin):
    title = models.TextField()
    description = models.TextField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    age_limit = models.IntegerField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    type = models.TextField()

    class Meta:
        db_table = 'book'


class BookAuthor(UUIDMixin, CreatedMixin):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    class Meta:
        db_table = 'book_author'
        unique_together = (('book', 'author'),)

class Genre(UUIDMixin, CreatedMixin, ModifiedMixin):
    name = models.TextField()
    description = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'genre'

class BookGenre(UUIDMixin, CreatedMixin):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    class Meta:
        db_table = 'book_genre'
        unique_together = (('book', 'genre'),)

