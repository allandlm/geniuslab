from django.shortcuts import get_object_or_404, render, redirect
from .models import Book
from django.contrib import messages

def home_view(request):
    return render(request, 'home.html')

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
        publication_year = request.POST.get('publication_year')
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
            publication_year=publication_year,
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

def edit_book(request, id):
    # Verifica se o usuário logado é administrador
    if request.user.user_type != 'admin':
        messages.error(request, "Você não tem permissão para editar livros.")
        return redirect('list_books')
    
    book = get_object_or_404(Book, id=id)  # Obtém o livro ou retorna 404 se não existir

    if request.method == 'POST':
        # Atualize os dados do formulário
        book.title = request.POST.get('title')
        book.author = request.POST.get('author')
        book.isbn = request.POST.get('isbn')
        book.publisher = request.POST.get('publisher')
        book.publication_year = request.POST.get('publication_year')
        book.genre = request.POST.get('genre')
        book.total_quantity = request.POST.get('total_quantity')
        book.available_quantity = request.POST.get('available_quantity')
        book.description = request.POST.get('description')

        # Salve as alterações no banco de dados
        book.save()
        messages.success(request, "Livro atualizado com sucesso!")
        
        # Redirecione para a lista de livros
        return redirect('list_books')

    return render(request, 'edit_book.html', {'book': book})

def delete_book(request, id):
    # Verifica se o usuário logado é administrador
    if request.user.user_type != 'admin':
        messages.error(request, "Você não tem permissão para excluir livros.")
        return redirect('list_books')
    
    book = get_object_or_404(Book, id=id)  # Obtém o livro ou retorna 404 se não existir
    book.delete()  # Exclui o livro do banco de dados
    messages.success(request, "Livro excluído com sucesso!")  # Exibe uma mensagem de sucesso
    
    # Redireciona para a lista de livros
    return redirect('list_books')