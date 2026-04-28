from django.shortcuts import render
from core.models import Produto
def index(request):
    context = {'produtos': Produto.objects.all()}
    return render(request, 'index.html', context)

def contato(request):
    return render(request, 'contato.html')

def produto(request, produto_id):
    context = {'produto': Produto.objects.get(id=produto_id)}
    return render(request, 'produto.html', context)