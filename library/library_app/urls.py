from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'Book', views.BookViewSet, basename='Book')
router.register(r'Genre', views.GenreViewSet, basename='Genre')
router.register(r'Author', views.AuthorViewSet, basename='Author')

urlpatterns = [
    path('', views.custom_main, name='homepage'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('genres', views.GenreListView.as_view(), name='genres'),
    path('book/', views.book_view, name='book'),
    path('genre/', views.genre_view, name='genre'),
    path('author/', views.author_view, name='author'),
    path('weather/', views.weather_page, name='weather'),
    # REST
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('rest/', include(router.urls)),
    path('rest/weather/', views.weather_rest)
]