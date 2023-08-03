from django.db import models

class Produto(models.Model):
    nome=models.CharField('Nome', max_length=100)
    preco=models.DecimalField('Preco', decimal_places=2, max_digits=8)
    ingredientes = models.TextField('Ingredientes', max_length=300)
    def __str__(self):
        return self.nome