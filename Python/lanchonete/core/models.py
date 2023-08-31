from django.db import models

# Create your models here.
class Cliente(models.Model):
    nome=models.CharField('Nome', max_length=100)
    cpf=models.CharField('cpf', max_length=11)
    rg=models.CharField('rg', max_length=11)
    endereco=models.CharField('endereco', max_length=100)
    def __str__(self):
        return self.nome
