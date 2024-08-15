from django.shortcuts import render
from django.http import HttpResponse
from .models import Aluno


def index(request):
    alunos = Aluno.objects.all()
    contexto = {
        'alunos': alunos,
    }
    return render(request, 'gerencia/index.html', contexto)


