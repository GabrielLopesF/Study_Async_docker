from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.messages import add_message, constants
from django.contrib import messages
from django.contrib import auth
def cadastro(request):
    if request.method == "GET":
        messages.add_message(request, constants.SUCCESS, 'Seja bem vindo!')
        return render(request, 'cadastro.html')

    elif request.method == "POST":
        username = request.POST.get('username')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')

        if not senha == confirmar_senha:
            messages.add_message(request, constants.WARNING, 'as senhas não coincidem')
            return redirect('/usuarios/cadastro')
        
        user = User.objects.filter(username=username)
        
        if user.exists():
            messages.add_message(request, constants.WARNING, 'já existe um usuario com esse username')
            return redirect('/usuarios/cadastro')
        try:
            User.objects.create_user(username=username, password=senha)
            messages.add_message(request, constants.SUCCESS, 'Cadastro realizado com sucesso, faça login para acessar a plataforma')
            return redirect('/usuarios/logar')
        except:
            messages.add_message(request, constants.ERROR('Erro interno do sistema contate o administrador'))
            return redirect('/usuarios/cadastro')

def logar(request):
    if request.method == "GET":
        return render(request, 'login.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = auth.authenticate(request, username=username, password=senha)

        if user:
            auth.login(request, user)
            messages.add_message(request, constants.SUCCESS, 'Logado')
            return redirect('/flashcard/novo_flashcard/')
        else:
            messages.add_message(request, constants.ERROR, 'username ou senha invalidos')
            return redirect('/usuarios/logar/')
        
def logout(request):
    auth.logout(request)
    
    return redirect('/usuarios/logar')