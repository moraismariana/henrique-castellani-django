from django.db import models

class Introducao(models.Model):
    titulo = models.CharField(max_length=100, null=False, blank=False)
    subtitulo = models.CharField(max_length=100)
    imagem = models.ImageField(upload_to='introducao', blank=False)

    # Configurações de Instância Única
    def save(self, *args, **kwargs):
        if not self.pk and Introducao.objects.exists():
            raise ValueError('Edite a introdução existente ao invés de criar uma.')
        return super(Introducao, self).save(*args, **kwargs)
    def delete(self, *args, **kwargs):
        if Introducao.objects.count() == 1:
            raise ValueError('Você não pode deletar a introdução.')
        super(Introducao, self).delete(*args, **kwargs)
    @classmethod
    def get_instance(cls):
        instance, created = cls.objects.get_or_create(pk=1)
        return instance

    class Meta:
        verbose_name_plural = "Introdução"

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

    # Configuração de instâncias
    def save(self, *args, **kwargs):
        if not self.pk and Servico.objects.count() == 3:
            raise ValueError('Edite a introdução existente ao invés de criar uma.')
        return super(Servico, self).save(*args, **kwargs)
    def delete(self, *args, **kwargs):
        if Servico.objects.count() == 3:
            raise ValueError('Você não pode deletar a introdução.')
        super(Servico, self).delete(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Serviços"

    def __str__(self):
        return self.servico
    
class Sobre(models.Model):
    descricao = models.TextField(null=False, blank=False)

    class Meta:
        verbose_name_plural = "Sobre mim"

    def __str__(self):
        return f'Parágrafo {self.id}'
    
class Contato(models.Model):
    telefone = models.CharField(max_length=50, null=False, blank=False)
    email = models.CharField(max_length=100, null=False, blank=False)
    endereco_1 = models.CharField(max_length=100)
    endereco_2 = models.CharField(max_length=100)
    imagem = models.ImageField(upload_to='contato', blank=False)

    # Configurações de Instância Única
    def save(self, *args, **kwargs):
        if not self.pk and Contato.objects.exists():
            raise ValueError('Edite a introdução existente ao invés de criar uma.')
        return super(Contato, self).save(*args, **kwargs)
    def delete(self, *args, **kwargs):
        if Contato.objects.count() == 1:
            raise ValueError('Você não pode deletar a introdução.')
        super(Contato, self).delete(*args, **kwargs)
    @classmethod
    def get_instance(cls):
        instance, created = cls.objects.get_or_create(pk=1)
        return instance

    class Meta:
        verbose_name_plural = "Contato"

    def __str__(self):
        return 'Contato'
    
class Portfolio(models.Model):
    imagem = models.ImageField(upload_to='portfolio', blank=False)
    alt = models.CharField(max_length=50, null=False, blank=False)

class Quadro_1(Portfolio):
    # Configuração de instâncias
    def save(self, *args, **kwargs):
        if not self.pk and Quadro_1.objects.count() == 3:
            raise ValueError('Edite as fotografias existentes ao invés de criar uma.')
        return super(Quadro_1, self).save(*args, **kwargs)
    def delete(self, *args, **kwargs):
        if Quadro_1.objects.count() == 3:
            raise ValueError('Você não pode deletar as fotografias.')
        super(Quadro_1, self).delete(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Portfolio - Quadro 1"
    def __str__(self):
        return f'Imagem {self.id}'
    
class Quadro_2(Portfolio):
    # Configuração de instâncias
    def save(self, *args, **kwargs):
        if not self.pk and Quadro_2.objects.count() == 2:
            raise ValueError('Edite as fotografias existentes ao invés de criar uma.')
        return super(Quadro_2, self).save(*args, **kwargs)
    def delete(self, *args, **kwargs):
        if Quadro_2.objects.count() == 2:
            raise ValueError('Você não pode deletar as fotografias.')
        super(Quadro_2, self).delete(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Portfolio - Quadro 2"
    def __str__(self):
        return f'Imagem {self.id}'
    
class Quadro_3(Portfolio):
    # Configuração de instâncias
    def save(self, *args, **kwargs):
        if not self.pk and Quadro_3.objects.count() == 3:
            raise ValueError('Edite as fotografias existentes ao invés de criar uma.')
        return super(Quadro_3, self).save(*args, **kwargs)
    def delete(self, *args, **kwargs):
        if Quadro_3.objects.count() == 3:
            raise ValueError('Você não pode deletar as fotografias.')
        super(Quadro_3, self).delete(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Portfolio - Quadro 3"
    def __str__(self):
        return f'Imagem {self.id}'
    
class Quadro_4(Portfolio):
    # Configuração de instâncias
    def save(self, *args, **kwargs):
        if not self.pk and Quadro_4.objects.count() == 2:
            raise ValueError('Edite as fotografias existentes ao invés de criar uma.')
        return super(Quadro_4, self).save(*args, **kwargs)
    def delete(self, *args, **kwargs):
        if Quadro_4.objects.count() == 2:
            raise ValueError('Você não pode deletar as fotografias.')
        super(Quadro_4, self).delete(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Portfolio - Quadro 4"
    def __str__(self):
        return f'Imagem {self.id}'