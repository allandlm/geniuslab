from django.shortcuts import render, redirect
from .models import Book
from django.contrib import messages

def list_books(request):
    books = Book.objects.all()  # Obtém todos os livros do banco de dados
    return render(request, 'list_books.html', {'books': books})

def add_book_view(request):
    if request.method == 'POST':
        # Obtenha os dados do formulário
        title = request.POST.get('title')
        author = request.POST.get('author')
        isbn = request.POST.get('isbn')
        publisher = request.POST.get('publisher')
        year = request.POST.get('year')
        genre = request.POST.get('genre')
        total_quantity = request.POST.get('total_quantity')
        available_quantity = request.POST.get('available_quantity')
        description = request.POST.get('description')

        # Crie uma nova instância de Book
        new_book = Book(
            title=title,
            author=author,
            isbn=isbn,
            publisher=publisher,
            year=year,
            genre=genre,
            total_quantity=total_quantity,
            available_quantity=available_quantity,
            description=description
        )

        # Salve o livro no banco de dados
        new_book.save()
        messages.success(request, "Livro cadastrado com sucesso!")
        
        # Redirecione para a lista de livros ou outra página desejada
        return redirect('list_books')

    return render(request, 'book_form.html')