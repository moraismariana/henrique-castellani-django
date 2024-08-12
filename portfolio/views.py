from django.shortcuts import render
from portfolio.models import Cliente, Servico, Sobre, Introducao, Contato, Quadro_1, Quadro_2, Quadro_3, Quadro_4, Portfolio

def index(request):
    clientes = Cliente.objects.all()
    servicos = Servico.objects.all()
    sobre = Sobre.objects.all()
    intro = Introducao.objects.all()
    contato = Contato.objects.all()
    quadro_1 = Quadro_1.objects.all()
    quadro_2 = Quadro_2.objects.all()
    quadro_3 = Quadro_3.objects.all()
    quadro_4 = Quadro_4.objects.all()
    portfolio = Portfolio.objects.all()
    return render(request, 'index.html', {'clientes': clientes, 'servicos':servicos, 'sobre':sobre, 'intro': intro, 'contato': contato, 'quadro_1': quadro_1, 'quadro_2': quadro_2, 'quadro_3': quadro_3, 'quadro_4': quadro_4, 'portfolio': portfolio})
