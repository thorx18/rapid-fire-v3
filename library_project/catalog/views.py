from django.shortcuts import render
from .models import Book, Author, BorrowedBook

def home(request):
    return render(request, 'index.html')

def books(request):
    all_books = Book.objects.all()        # ✅ from DB
    return render(request, 'books.html', {'books': all_books})

def authors(request):
    all_authors = Author.objects.all()    # ✅ from DB
    return render(request, 'authors.html', {'authors': all_authors})

def borrowed(request):
    borrowed_books = BorrowedBook.objects.all()  # ✅ from DB
    return render(request, 'borrowed.html', {'borrowed': borrowed_books})