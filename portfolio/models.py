from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    comentario = models.TextField(null=False, blank=False)
    foto = models.ImageField(upload_to="clientes", blank=False)

    def __str__(self):
        return self.nome
    
class Servico(models.Model):
    servico = models.CharField(max_length=100, null=False, blank=False)
    imagem = models.ImageField(upload_to="servicos", blank=False)

    def __str__(self):
        return self.servico
    
class Sobre(models.Model):
    descricao = models.TextField(null=False, blank=False)

    def __str__(self):
        return f'Parágrafo {self.id}'