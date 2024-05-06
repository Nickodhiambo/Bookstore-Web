from django.urls import path
from .views import BookListView, BookDetailView, AddBookCreateView, SearchResultsListView

urlpatterns = [
        path('', BookListView.as_view(), name='book-list'),
        path('<uuid:pk>/', BookDetailView.as_view(), name='book-detail'),
        path('search/', SearchResultsListView.as_view(),
            name='search-results'),
        path('add_book/', AddBookCreateView.as_view(), name='add-book'),
]
