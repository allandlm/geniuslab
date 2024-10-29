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

from geniuslab.books.views import add_book_view, list_books
from geniuslab.loans.views import register_loan, return_loan
from geniuslab.reports.views import generate_report
from geniuslab.users.views import register_user


urlpatterns = [
    path('admin/', admin.site.urls), # URL entrar como admin
    path('livros/', list_books, name='list_books'),  # URL para listar livros
    path('livros/adicionar/', add_book_view, name='add_book'),  # URL para adicionar livro
    path('registrar/', register_user, name='register_user'),  # URL para registrar usuário
    path('registrar-empréstimo/', register_loan, name='register_loan'),  # URL para registrar empréstimo
    path('devolver-empréstimo/', return_loan, name='return_loan'),  # URL para registrar devolução
    path('relatorio-empréstimos/', generate_report, name='generate_report'),  # URL para gerar relatório


    # Adicione outras URLs conforme necessário
]
