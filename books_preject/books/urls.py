from django.contrib import admin
from django.urls import path, include

from .views import BookListView, BookCreateView, BookUpdateView
from .views import signup
urlpatterns = [
    path('', BookListView.as_view(), name='book_list'),
    path('book_create/', BookCreateView.as_view(), name='book_create'),
path('book_edit/<int:pk>/', BookUpdateView.as_view(), name='book_edit'),  # Add this line
    path('signup/', signup, name='signup'),

    #quero fazer o login e o logout
    path('login/', include('django.contrib.auth.urls'), name='login'),
    path('logout/', include('django.contrib.auth.urls'), name='logout'),
]
