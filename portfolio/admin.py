from django.contrib import admin
from portfolio.models import Cliente, Servico, Sobre, Introducao, Contato, Quadro_1, Quadro_2, Quadro_3, Quadro_4

def limite_instancia(limite):
    class InstanciaLimite(admin.ModelAdmin):
        def has_add_permission(self, request):
            if self.model.objects.count() == limite:
                return False
            return super().has_add_permission(request)
        
        def has_delete_permission(self, request, obj=None):
            if self.model.objects.count() == limite:
                return False
            return super().has_delete_permission(request, obj)
    return InstanciaLimite

admin.site.register(Introducao, limite_instancia(1))
admin.site.register(Sobre)
admin.site.register(Servico, limite_instancia(3))
admin.site.register(Cliente)
admin.site.register(Contato, limite_instancia(1))
admin.site.register(Quadro_1, limite_instancia(3))
admin.site.register(Quadro_2, limite_instancia(2))
admin.site.register(Quadro_3, limite_instancia(3))
admin.site.register(Quadro_4, limite_instancia(2))