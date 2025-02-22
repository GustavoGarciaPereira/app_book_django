from django.contrib import admin
from django.urls import path, include

from .views import (
    BookListView,
    BookCreateView,
    BookUpdateView,
    BookDetailView,
    BookDeleteView
)

urlpatterns = [
    path('', BookListView.as_view(), name='book_list'),
    path('book_create/', BookCreateView.as_view(), name='book_create'),
    path('book_edit/<int:pk>/', BookUpdateView.as_view(), name='book_edit'),  # Add this line
    path('book_detail/<int:pk>/', BookDetailView.as_view(), name='book_detail'),  # Add this line
    path('book_delete/<int:pk>/', BookDeleteView.as_view(), name='book_delete'),
]