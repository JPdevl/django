from django.contrib import admin
from django.urls import path
from app1.views import listaClientes, listaPedidos, listaProdutos, detalharClientes, detalharPedidos, detalharProdutos, editarClientes, editarProdutos, editarPedidos, excluirClientes, excluirPedidos, excluirProdutos
#index_int,index_str, index_hora


#path('<int:valor>', index_int),
#path('<str:valor>', index_str),

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('saudacao/<str:nome>/', index_hora),
    path('listaClientes/', listaClientes, name="listaClientes"),
    path('listaProdutos/', listaProdutos, name="listaProdutos"),
    path('listaPedidos/', listaPedidos, name="listaPedidos"),
    path('detalharClientes/<int:id>', detalharClientes, name = "detalharClientes"),
    path('detalharProdutos/<int:id>', detalharProdutos, name = "detalharProdutos"),
    path('detalharPedidos/<int:id>', detalharPedidos, name = "detalharPedidos"),    
    path('editarClientes/<int:id>', editarClientes, name = "editarClientes"),
    path('editarProdutos/<int:id>', editarProdutos, name = "editarProdutos"),
    path('editarPedidos/<int:id>', editarPedidos, name = "editarPedidos"),
    path('excluirClientes/<int:id>', excluirClientes, name = "excluirClientes"),
    path('excluirProdutos/<int:id>', excluirProdutos, name = "excluirProdutos"),
    path('excluirPedidos/<int:id>', excluirPedidos, name = "excluirPedidos"),
    
    
    
    
]