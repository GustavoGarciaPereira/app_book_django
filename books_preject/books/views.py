from django.contrib import messages
from django.shortcuts import redirect, render

# Create your views here.
# views.py
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Book
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin

class BookListView(LoginRequiredMixin, ListView):
    model = Book
    template_name = 'books/list.html'
    context_object_name = 'books'
    
    # def get_queryset(self):
    #     return Book.objects.filter(user=self.request.user)

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(user=self.request.user)
        search_query = self.request.GET.get('q')
        status_filter = self.request.GET.get('status')
        if search_query:
            queryset = queryset.filter(
                Q(title__icontains=search_query) | 
                Q(author__icontains=search_query)
            )
        if status_filter:
            queryset = queryset.filter(status=status_filter)
        
        return queryset

# views.py
class BookCreateView(LoginRequiredMixin, CreateView):
    model = Book
    fields = ['title', 'author', 'status', 'rating']
    template_name = 'books/form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('book_list')  # Redirect to the book list view after creation

# Implementar similar para UpdateView e DeleteView


# views.py (modificação do BookListView)
# views.py
from django.urls import reverse_lazy
from django.views.generic import UpdateView, TemplateView
from .models import Book

class BookUpdateView(LoginRequiredMixin, UpdateView):
    model = Book
    fields = ['title', 'author', 'status', 'rating']
    template_name = 'books/form.html'
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('book_list')  # Redirect to the book list view after updating

class BookDetailView(LoginRequiredMixin, UpdateView):
    model = Book
    fields = ['title', 'author', 'status', 'rating']
    template_name = 'books/form.html'
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('book_list')  # Redirect to the book list view after updating
    
class BookDeleteView(LoginRequiredMixin, UpdateView):
    model = Book
    fields = ['title', 'author', 'status', 'rating']
    template_name = 'books/form.html'
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('book_list')  # Redirect to the book list view after updating


# Em notes/views.py
from .forms import SignUpForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Conta criada para {username}!')
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


# views.py
from django.http import JsonResponse
from django.db.models import Count

def reading_stats(request):
    data = {
        'labels': ['Lidos', 'Desejados'],
        'data': [
            Book.objects.filter(user=request.user, status='Lido').count(),
            Book.objects.filter(user=request.user, status='Desejado').count(),
        ]
    }
    return JsonResponse(data)


class GraficoTemplateView(TemplateView):
    template_name = 'books/grafico.html'
    
    
# views.py
import csv
from django.http import HttpResponse

def export_books(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="meus_livros.csv"'

    writer = csv.writer(response)
    writer.writerow(['Título', 'Autor', 'Status', 'Avaliação'])

    books = Book.objects.filter(user=request.user)
    for book in books:
        writer.writerow([book.title, book.author, book.status, book.rating or 'N/A'])

    return response