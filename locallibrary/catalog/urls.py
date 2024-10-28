from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('book/<int:pk>/', views.BookDetailView.as_view(), name='book-detail'),  # Asegúrate de que hay un '/' al final
    path('author/<int:pk>/', views.AuthorDetailView.as_view(), name='author-detail'),
]
