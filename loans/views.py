from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Loan, User, Book  # Importe os modelos necessários
from django.utils import timezone

def register_loan(request):
    if request.method == 'POST':
        user_id = request.POST.get('user')
        book_id = request.POST.get('book')
        loan_date = request.POST.get('loan_date')
        return_date = request.POST.get('return_date')
        status = request.POST.get('status')

        # Verifica se o livro está disponível para empréstimo
        book = Book.objects.get(id=book_id)
        if book.available_quantity <= 0:
            messages.error(request, "Este livro não está disponível para empréstimo.")
            return redirect('register_loan')

        # Cria o empréstimo
        loan = Loan(
            user_id=user_id,
            book_id=book_id,
            loan_date=loan_date,
            return_date=return_date,
            status=status
        )
        loan.save()

        # Atualiza a quantidade disponível do livro
        book.available_quantity -= 1
        book.save()

        messages.success(request, "Empréstimo registrado com sucesso.")
        return redirect('list_loans')  # Redireciona para a lista de empréstimos

    # Se não for POST, renderiza o formulário
    users = User.objects.all()  # Obtem todos os usuários
    books = Book.objects.filter(available_quantity__gt=0)  # Obtem livros disponíveis
    loan_date_today = timezone.now().date()  # Obtém a data atual

    return render(request, 'loan_form.html', {
        'users': users,
        'books': books,
        'loan_date_today': loan_date_today
    })
    
def return_loan(request):
    if request.method == 'POST':
        loan_id = request.POST.get('loan')
        return_date = request.POST.get('return_date')
        observations = request.POST.get('observations')

        try:
            # Busca o empréstimo correspondente
            loan = Loan.objects.get(id=loan_id)

            # Atualiza a data de devolução e o status do empréstimo
            loan.return_date = return_date
            loan.status = 'Concluído'  # Atualiza o status para concluído
            loan.save()

            # Atualiza a quantidade disponível do livro
            book = loan.book
            book.available_quantity += 1  # Incrementa a quantidade disponível
            book.save()

            messages.success(request, "Devolução registrada com sucesso.")
            return redirect('list_loans')  # Redireciona para a lista de empréstimos
        except Loan.DoesNotExist:
            messages.error(request, "Empréstimo não encontrado.")
            return redirect('return_loan')

    # Se não for um POST, renderiza o formulário
    active_loans = Loan.objects.filter(status='Em Aberto')  # Obtém empréstimos ativos
    return_date_today = timezone.now().date()  # Obtém a data atual

    return render(request, 'loan_return_form.html', {
        'active_loans': active_loans,
        'return_date_today': return_date_today
    })
