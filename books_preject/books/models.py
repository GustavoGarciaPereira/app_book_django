from django.db import models

# Create your models here.
# models.py
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
class Book(models.Model):
    STATUS_CHOICES = [('Lido', 'Lido'), ('Desejado', 'Desejado')]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    rating = models.IntegerField(blank=True, null=True)  # Opcional para fase 2
    created_at = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
            return reverse('book_list')  # Redirect to the book list view after creation

    class Meta:
        unique_together = ['user', 'title', 'author']  # Evita duplicatas