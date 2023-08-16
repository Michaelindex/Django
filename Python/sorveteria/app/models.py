from django.db import models

# Create your models here.
class cliente(models.Model):
    nome= models.CharField('Nome', max_length=100, default='cat')
    cpf=models.CharField('cpf', max_length=11, default='cat')
    rg=models.CharField('rg', max_length=11, default='cat')
    logradouro=models.CharField('logradouro', max_length=100, default='cat')
    cidade=models.CharField('cidade', max_length=100, default='cat')
    uf=models.CharField('uf', max_length=2, default='cat')
    def __str__(self):
        return self.nome
    
class Produto(models.Model):
    nome = models.CharField('Nome', max_length=100, default='cat')
    preco = models.DecimalField('Preco', decimal_places=2, max_digits=8, default='cat')
    categoria=models.CharField('categoria', max_length=40, default='cat')
    sabor=models.CharField('sabor', max_length=20, default='cat')
    ingredientes=models.TextField('Ingredientes', max_length=300, default='cat')
    def __str__(self):
        return self.sabor