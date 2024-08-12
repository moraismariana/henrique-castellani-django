from django.shortcuts import render
from portfolio.models import Cliente, Servico

def index(request):
    clientes = Cliente.objects.all()
    servicos = Servico.objects.all()
    return render(request, 'index.html', {'clientes': clientes, 'servicos':servicos,})
