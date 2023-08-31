from django.db import models

# Create your models here.
class Lanche(models.Model):
    nome=models.CharField('Nome', max_length=100)
    preco=models.DecimalField('Preco', decimal_places=2, max_digits=8)
    categoria=models.CharField('Categoria', max_length=20, default='cat')
    ingredientes = models.TextField('Ingredientes', max_length=300)
    def __str__(self):
        return self.nome
    