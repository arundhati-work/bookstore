from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from .forms import BookForm

# Create your views here.
def home_page(request):
    return render(request, "home_page.html")

def list_books(request):
    books = Book.objects.all()
    context = {
        "books" : books
    }
    return render(request, "list_books.html", context)

def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    context = {
        "book":book
    }
    return render(request, "book_detail.html", context)

def create_book(request):
    if request.method=="GET":
        form = BookForm()
        context = {
            "form":form,
            "book": None
        }
        return render(request,"book_form.html",context)
    else:
        form = BookForm(request.POST)
        if form.is_valid():
            book_instance = form.save()
            return redirect("book_detail",book_id=book_instance.id)

def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "GET":
        form = BookForm(instance=book)
        context = {
            "form":form,
            "book":book
        }
        return render(request, "book_form.html", context)
    else:
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            book_instance = form.save()
            return redirect("book_detail",book_id=book_instance.id)

def delete_book(request,book_id):
    book = get_object_or_404(Book, id=book_id)
    context = {
        "book":book
    }
    if request.method == "GET":
        return render(request, 'delete_book.html', context)
    else:
        book.delete()
        return redirect('list_books')

