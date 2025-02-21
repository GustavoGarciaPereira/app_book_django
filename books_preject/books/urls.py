from django.contrib import admin
from django.urls import path, include

from .views import BookListView, BookCreateView, BookUpdateView
urlpatterns = [
    path('', BookListView.as_view(), name='book_list'),
    path('book_create/', BookCreateView.as_view(), name='book_create'),
    path('book_edit/<int:pk>/', BookUpdateView.as_view(), name='book_edit'),  # Add this line

    #quero fazer o login e o gustavo_g

]