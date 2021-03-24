from django import forms
from produtos.models import Produtos

class produtosForm(forms.ModelForm):

    class Meta:
        model = Produtos
        fields = ["codigo_produto","nome_produto","quantidade_produto","valor_por_kilo","validade_produto"]