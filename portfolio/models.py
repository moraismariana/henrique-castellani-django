from django.db import models

class Introducao(models.Model):
    titulo = models.CharField(max_length=100, null=False, blank=False)
    subtitulo = models.CharField(max_length=100)
    imagem = models.ImageField(upload_to='introducao', blank=False)

    def __str__(self):
        return 'Introdução'

class Cliente(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    comentario = models.TextField(null=False, blank=False)
    foto = models.ImageField(upload_to='clientes', blank=False)

    def __str__(self):
        return self.nome
    
class Servico(models.Model):
    servico = models.CharField(max_length=100, null=False, blank=False)
    imagem = models.ImageField(upload_to='servicos', blank=False)

    def __str__(self):
        return self.servico
    
class Sobre(models.Model):
    descricao = models.TextField(null=False, blank=False)

    def __str__(self):
        return f'Parágrafo {self.id}'
    
class Contato(models.Model):
    telefone = models.CharField(max_length=50, null=False, blank=False)
    email = models.CharField(max_length=100, null=False, blank=False)
    endereco_1 = models.CharField(max_length=100)
    endereco_2 = models.CharField(max_length=100)
    imagem = models.ImageField(upload_to='contato', blank=False)

    def __str__(self):
        return 'Contato'
    
class Portfolio(models.Model):
    imagem = models.ImageField(upload_to='portfolio', blank=False)
    alt = models.CharField(max_length=50, null=False, blank=False)

class Quadro_1(Portfolio):
    def __str__(self):
        return f'Imagem {self.id}'
    
class Quadro_2(Portfolio):
    def __str__(self):
        return f'Imagem {self.id}'
    
class Quadro_3(Portfolio):
    def __str__(self):
        return f'Imagem {self.id}'
    
class Quadro_4(Portfolio):
    def __str__(self):
        return f'Imagem {self.id}'