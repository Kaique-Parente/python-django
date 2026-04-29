from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import ContatoForm

def index(request):
    return render(request, 'index.html')

def contato(request):
    form = ContatoForm(request.POST or None)

    if str(request.method) == 'POST':
        if form.is_valid():
            data = form.cleaned_data
            print(data)

            form.send_mail()
            messages.success(request, 'Contato enviado com sucesso!')
            return redirect('contato')
        else:
            messages.error(request, 'Erro ao enviar o formulário')

    return render(request, 'contato.html', {'form': form})

def produto(request):
    return render(request, 'produto.html')