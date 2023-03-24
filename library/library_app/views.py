from django.shortcuts import render
from .models import Book, Genre, Author
from django.views.generic import ListView
from django.core.paginator import Paginator


PAGINATOR_THRESHOLD = 20

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

def catalog_view(cls_model, context_name, template):
    class CustomListView(ListView):
        model = cls_model
        template_name = template
        paginate_by = PAGINATOR_THRESHOLD
        context_object_name = context_name

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            objects = cls_model.objects.all()
            paginator = Paginator(objects, PAGINATOR_THRESHOLD)
            page = self.request.GET.get('page')
            page_obj = paginator.get_page(page)
            context[f'{context_name}_list'] = page_obj
            return context

    return CustomListView

CATALOG = 'catalog'
BOOKS_CATALOG = f'{CATALOG}/books.html'
AUTHORS_CATALOG = f'{CATALOG}/authors.html'
GENRES_CATALOG = f'{CATALOG}/genres.html'

BookListView = catalog_view(Book, 'books', BOOKS_CATALOG)
AuthorListView = catalog_view(Author, 'authors', AUTHORS_CATALOG)
GenreListView = catalog_view(Genre, 'genres', GENRES_CATALOG)