from urllib import request
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib.auth.decorators import login_required

User = get_user_model()

def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = User.objects.get(email=email)
            user = authenticate(request, username=user.username, password=password)
        except User.DoesNotExist:
            user = None

        if user is not None:
            login(request, user)
            if user.user_type == User.ADMIN:
                return redirect('admin_dashboard.html')
            else:
                return redirect('reader_dashboard.html')
        else:
            messages.error(request, "Email ou senha incorretos.")
            return redirect('login')
    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('login')

@login_required
def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')

@login_required
def reader_dashboard(request):
    return render(request, 'reader_dashboard.html')

def register_user(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        user_type = request.POST.get('user_type')
        address = request.POST.get('address')
        phone = request.POST.get('phone')

        # Verifica se as senhas são iguais
        if password != confirm_password:
            messages.error(request, "As senhas não coincidem.")
            return redirect('register_user')

        # Verifica se o e-mail já está em uso
        if User.objects.filter(email=email).exists():
            messages.error(request, "Este e-mail já está cadastrado.")
            return redirect('register_user')

        # Cria o usuário
        user = User.objects.create_user(
            username=full_name,
            email=email,
            password=password,
            first_name=full_name,
            user_type=user_type,
            address=address,
            phone=phone
        )
        
        user.save()

        # Aqui você pode armazenar o tipo de usuário em um perfil separado se desejar

        messages.success(request, "Usuário cadastrado com sucesso.")
        return redirect('login')  # Redireciona para a página de login (ou outra página desejada)

    return render(request, 'user_registration.html')

def list_users(request):
    users = User.objects.all()  # Obtém todos os usuários
    return render(request, 'list_users.html', {'users': users})