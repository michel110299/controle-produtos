from django.shortcuts import render,redirect
from produtos.models import Produtos
from produtos.forms import produtosForm 
from django.contrib import messages



def registrar_produto(request):

    form = produtosForm() 

    if request.method == "POST":

        form = produtosForm(request.POST)

        if form.is_valid():

            produto = form.save(commit=False)
            nome = produto.nome_produto

            produto.nome_produto = nome.title()

            produto.save()

            return redirect("index")



    context = {
         "form": form
    }

    return render(request,"registrar_produto.html",context)

def vender_produto(request):

    if request.POST:    
        codigo_produto = request.POST.get("produto_para_vender",None)
        quantidade = int(request.POST.get("quantidade_para_vender",None))

        try:
            produto = Produtos.objects.get(codigo_produto__contains=codigo_produto)

        except Produtos.DoesNotExist:
            messages.error(request,"Produto não encontrado")
        
        if produto.venda(quantidade):
            messages.success(request,"Produto vendido com sucesso!")
            produto.save()
        else:
            messages.error(request,"não temos essa quantidade em estoque!")

        
        return redirect("index")

        # todos_produtos = Produtos.objects.all()


        # for x in todos_produtos:
        #     if x.nome_produto == nome.title():
        #         if x.venda(quantidade) == False :
        #             x.delete()
        #             return redirect("index")
                
        #         x.save()
        #         return redirect("index")
    return render(request , "venda_produto.html")