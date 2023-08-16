from django.contrib import admin
from .models import cliente, Produto
# Register your models here.

class ListaCliente(admin.ModelAdmin):
    list_display=('id', 'nome', 'cpf', 'logradouro', 'cidade')
    list_display_links=('id', 'nome')
    search_fields=('nome', 'cpf', 'logradouro', 'cidade')
    list_filter=('cidade',)
    list_editable=('logradouro', 'cidade')
    list_per_page=2

admin.site.register(cliente, ListaCliente)
admin.site.register(Produto)