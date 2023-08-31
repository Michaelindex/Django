from django.shortcuts import render

# Create your views here.
def index(requests):
    return render(requests, 'index.html')
def contato(requests):
    return render(requests, 'contato.html')