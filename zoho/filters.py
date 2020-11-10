import django_filters
from .models import Book

class BookFilter(django_filters.FilterSet):
    author = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Book
        fields = '__all__'
        exclude = ('puplished_at','the_book', 'about_book')
