from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Apostila, ViewApostila
from django.contrib.messages import constants
from django.contrib import messages
# Create your views here.
def adicionar_apostilas(request):
    if request.method =="GET":
        apostilas = Apostila.objects.filter(user=request.user)

        
        return render(request, 'adicionar_apostilas.html', {'apostilas':apostilas,})
    elif request.method == "POST":
        titulo = request.POST.get('titulo')
        arquivo = request.FILES['arquivo']

        apostila = Apostila(
            user = request.user,
            titulo=titulo,
            arquivo=arquivo,
        )
        apostila.save()
        messages.add_message(request, constants.SUCCESS, 'Salvo com sucesso')

        return redirect('/apostilas/adicionar_apostilas')

def apostila(request, id):
    apostila = Apostila.objects.get(id=id)
    
    view = ViewApostila(
        ip=request.META['REMOTE_ADDR'],
        apostila=apostila
    )
    view.save()
    return render(request, 'apostila.html', {'apostila': apostila})