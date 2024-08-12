from django.shortcuts import render
from portfolio.models import Cliente

def index(request):
    clientes = Cliente.objects.all()
    return render(request, 'index.html', {'clientes': clientes})
