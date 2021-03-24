from django.contrib import admin
from django.urls import path
from dashboard.views import index
from produtos.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('registrar-produto/', registrar_produto, name="registrar_produto"),
    path('venda-produto/', vender_produto, name="venda_produto"),
]
