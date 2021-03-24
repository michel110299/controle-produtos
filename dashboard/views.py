from django.shortcuts import render
from produtos.models import Produtos

def index(request):
    todos_produtos = Produtos.objects.all()

    context = {
        "todos_produtos" : todos_produtos,
    }

    return render(request,"index.html",context )


