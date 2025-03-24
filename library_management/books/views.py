from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework import status
from .models import Book
from .serializers import BookSerializer
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

class IsAuthenticated(permissions.BasePermission):
    def has_permission(self, request, view):
        if view.action == 'list':
            return True
        return request.user and request.user.is_authenticated

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

def student_book_list(request):
    books = Book.objects.all()
    return render(request, 'books/student_list.html', {'books': books})

@login_required
def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/list.html', {'books': books})

@login_required
def book_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        isbn = request.POST.get('isbn')
        publication_year = request.POST.get('publication_year')
        genre = request.POST.get('genre')
        description = request.POST.get('description')
        
        Book.objects.create(
            title=title,
            author=author,
            isbn=isbn,
            publication_year=publication_year,
            genre=genre,
            description=description
        )
        messages.success(request, 'Book created successfully')
        return redirect('book_list')
    
    return render(request, 'books/create.html')

@login_required
def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    
    if request.method == 'POST':
        book.title = request.POST.get('title')
        book.author = request.POST.get('author')
        book.isbn = request.POST.get('isbn')
        book.publication_year = request.POST.get('publication_year')
        book.genre = request.POST.get('genre')
        book.description = request.POST.get('description')
        book.save()
        
        messages.success(request, 'Book updated successfully')
        return redirect('book_list')
    
    return render(request, 'books/update.html', {'book': book})

@login_required
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    
    if request.method == 'POST':
        book.delete()
        messages.success(request, 'Book deleted successfully')
        return redirect('book_list')
    
    return render(request, 'books/delete.html', {'book': book})