from .models import Book, Review
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import (
        LoginRequiredMixin,
        PermissionRequiredMixin
        )
from django.db.models import Q
from .forms import ReviewForm
from django.shortcuts import redirect
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy


# Create your views here.
class BookListView(LoginRequiredMixin, ListView):
    """Displays a list of books"""
    model = Book
    context_object_name = 'book_list'
    template_name = 'books/book_list.html'
    login_url = 'account_login'

class BookDetailView(
        LoginRequiredMixin,
        DetailView
        ):
    """Displays details of a given book"""
    model = Book
    context_object_name = 'book'
    template_name = 'books/book_detail.html'
    login_url = 'account_login'
    #permission_required = 'books.special_status'

    def get_context_data(self, **kwargs):
        """Overrides DetailView context dictionary
        to add a review form to the context
        """
        context = super().get_context_data(**kwargs)
        context['form'] = ReviewForm()
        return context

    def post(self, request, *args, **kwargs):
        """submits review data"""
        form = ReviewForm(request.POST)
        if form.is_valid():
            book = self.get_object()
            review = form.save(commit=False)
            review.book = book
            review.author = request.user
            review.save()
            return redirect('book-detail', pk=book.pk)
        else:
            # If form is not valid, re-render the page with errors
            return self.get(request, *args, **kwargs)


class AddBookCreateView(CreateView):
    """Adds a book to db"""
    model = Book
    fields = ['title', 'author', 'price', 'cover']
    template_name = 'books/add_book.html'
    success_url = reverse_lazy('book-list')

class SearchResultsListView(ListView):
    model = Book
    context_object_name = 'book_list'
    template_name = 'books/search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Book.objects.filter(
                Q(title__icontains=query) | Q(author__icontains=query)
                )
