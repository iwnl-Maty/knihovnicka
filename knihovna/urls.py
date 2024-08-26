from django.urls import path
from .views import BooksListView, index, BooksDetailView

urlpatterns = [
    path('', index, name='index'),
    path('books/', BooksListView.as_view(), name='books_list'),
    path('books/<int:pk>', BooksDetailView.as_view(), name='books_detail'),
]
