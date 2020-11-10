from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm
from .filters import BookFilter
# Create your views here.

def booklist(request):
    books = Book.objects.all()

    myfilter = BookFilter(request.GET, queryset=books)
    books = myfilter.qs
    context = {
        'books': books,
        'myfilter':myfilter

    }
    return render(request,'book.html', context)


def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST,  request.FILES)
        if form.is_valid():
            form.save()

            return redirect('home:book')

    else:
        form=BookForm()

    cotext= {
        'form': form
    }


    return render(request, 'add.html', cotext)

