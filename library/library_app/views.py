from django.shortcuts import render
from .models import Book, Genre, Author

TEMPLATE_MAIN = 'index.html'

def custom_main(request):
    return render(
        request,
        TEMPLATE_MAIN,
        context={
            'books': Book.objects.all().count(),
            'genres': Genre.objects.all().count(),
            'authors': Author.objects.all().count(),
        }
    )