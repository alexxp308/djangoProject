from django.shortcuts import render
from .models import Book,Author,BookInstance,Genre
from django.views import generic
from django.http import *

def index(request):
    num_books=Book.objects.all().count()
    num_instances=BookInstance.objects.all().count()
    num_instances_available=BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.count()

    return render(
        request,
        'index.html',
        context={'num_books':num_books,
                 'num_instances':num_instances,
                 'num_instances_available': num_instances_available,
                 'num_authors':num_authors},
    )

class BookListView(generic.ListView):
    model = Book
    paginate_by = 2

def  book_detail_view(request,pk):
    try:
        book_id=Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        raise Http404("Book does not exist")
    # book_id=get_object_or_404(Book, pk=pk)

    return render(
        request,
        'catalog/book_detail.html',
        context={'book':book_id,}
    )

class BookDetailView(generic.DetailView):
    model = Book