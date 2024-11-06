"""
URL configuration for geniuslab project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from books.views import add_book_view, delete_book, edit_book, home_view, list_books
from loans.views import loan_history, register_loan, return_loan
from reports.views import generate_report
from users.views import admin_dashboard, list_users, reader_dashboard, register_user, user_login, user_logout

urlpatterns = [
    # ===== Controle dev =====
    path('home/', home_view, name='home'),  # URL para página inicial
    path('admin/', admin.site.urls), # URL entrar como superuser
    
    # ===== Login e Logout =====
    path('', user_login, name='login'), # URL para login
    path('logout/', user_logout, name='logout'), # URL para logout
    
    # ===== Areas de admin e leitor =====
    path('administrador/', admin_dashboard, name='admin_dashboard'), # URL para area do admin
    path('leitor/', reader_dashboard, name='reader_dashboard'), # URL para area do leitor
    
    # ===== Livros =====
    path('livros/', list_books, name='list_books'),  # URL para listar livros
    path('livros/adicionar/', add_book_view, name='add_book'),  # URL para adicionar livro
    path('book/edit/<int:id>/', edit_book, name='edit_book'), # URL para editar livro
    path('book/delete/<int:id>/', delete_book, name='delete_book'),
   
    # ===== Usuários =====
    path('usuarios/', list_users, name='list_users'),  # URL para listar usuários
    path('registrar/', register_user, name='register_user'),  # URL para registrar usuário
   
    # ===== Empréstimos =====
    path('registrar-empréstimo/', register_loan, name='register_loan'),  # URL para registrar empréstimo
    path('devolver-empréstimo/', return_loan, name='return_loan'),  # URL para registrar devolução
    path('historico-emprestimos/', loan_history, name='loan_history'), # URL para listar empréstimos
    
    # ===== Relatórios =====
    path('relatorio-empréstimos/', generate_report, name='generate_report'),  # URL para gerar relatório


]
