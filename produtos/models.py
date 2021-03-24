from django.db import models

class Produtos(models.Model):

    nome_produto = models.CharField(
        verbose_name = "Produto",
        max_length = 194,
    )
    codigo_produto = models.CharField(
        verbose_name = "Codigo do produto",
        max_length = 194,
        null = True,
        blank = True,
    )
    quantidade_produto =  models.IntegerField(
        verbose_name = "Quantidade do produto",
    )
    valor_por_kilo = models.DecimalField(
        verbose_name = "Valor do produto",
        max_digits=7,
        decimal_places=2,
    )
    validade_produto = models.DateField(
        verbose_name = "Data de validade",
        auto_now = False,
        auto_now_add = False,
    )
    data_entrega = models.DateField(
        verbose_name = "Data da entrega",
        auto_now_add = True,
    )
    
    def venda(self,qtd):
        if self.quantidade_produto >= qtd:
            self.quantidade_produto -= qtd
            return True

        return False
    
    class meta:
        verbose_name = "Produto"
        db_table = "Produto"
    
    def __str__(self):
        return self.nome_produto
