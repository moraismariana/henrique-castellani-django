from django.contrib import admin
from portfolio.models import Cliente, Servico, Sobre

admin.site.register(Sobre)
admin.site.register(Servico)
admin.site.register(Cliente)