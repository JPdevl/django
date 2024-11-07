from django.shortcuts import render, redirect
from datetime import datetime
from app1.models import Cliente, Pedido, Produto
# Create your views here.


def listaClientes(request):
    return render(request, 'listaClientes.html',{'listaClientes':Cliente.objects.all()})

def listaProdutos(request):
    return render(request, 'listaProdutos.html',{'listaProdutos':Produto.objects.all()})

def listaPedidos(request):
    return render(request, 'listaPedidos.html',{'listaPedidos':Pedido.objects.all()})

def detalharClientes(request, id):
    return render(request, 'detalharClientes.html', {'dadosCliente':Cliente.objects.get(id=id)})

def detalharProdutos(request, id):
    return render(request, 'detalharProdutos.html', {'dadosProduto':Produto.objects.get(id=id)})

def detalharPedidos(request, id):
    return render(request, 'detalharPedidos.html', {'dadosPedido':Pedido.objects.get(id=id)})

def editarClientes(request,id):
    cliente = Cliente.objects.get(id=id)
    if request.method == "POST":
       cliente.nome = request.POST.get("nome")
       cliente.cpf = request.POST.get("cpf")
       cliente.endereco = request.POST.get("endereco")
       cliente.data_nascimento = request.POST.get("data_nascimento")

       cliente.save()

       return redirect('listaClientes')
    else:
       return render(request, 'editarClientes.html', {'dadosCliente':cliente})
    
def editarProdutos(request,id):
    produtos = Produto.objects.get(id=id)
    if request.method == "POST":
        
       produtos.cod = request.POST.get("cod")
       produtos.nome = request.POST.get("nome")
       produtos.valor_unitario = request.POST.get("valor")
       
       produtos.save()

       return redirect('listaProdutos')
    else:
       return render(request, 'editarProdutos.html', {'dadosPedido':produtos})
   
   
def editarPedidos(request,id):
    pedidos = Pedido.objects.get(id=id)
    if request.method == "POST":
       pedidos.data = request.POST.get("data")
       pedidos.valor = request.POST.get("valor")
       pedidos.descricao = request.POST.get("descricao")
       pedidos.id_cliente = request.POST.get("id_cliente")
       pedidos.id_produto = request.POST.get("id_produto")

       pedidos.save()

       return redirect('listaPedidos')
    else:
       return render(request, 'editarPedidos.html', {'dadosPedido':pedidos})


def excluirClientes(request, id):
    return render(request, 'excluirClientes.html')

def excluirProdutos(request, id):
    return render(request, 'excluirProdutos.html')

def excluirPedidos(request, id):
    return render(request, 'excluirPedidos.html')


"""
#def index_int(request, valor):
    #return render(request, 'index.html', {'valor':valor, 'tipo': 'int'})
3
#def index_str(request, valor):
    #return render(request, 'index.html', {'valor':valor, 'tipo': 'str'})

def index_hora(request, nome):
    hora_agora = datetime.now().hour
    minuto_agora = datetime.now().minute

    if hora_agora > 5 and hora_agora < 12:
        saudacao = (f"Bom dia {nome}!")
    elif hora_agora > 12 and hora_agora < 18:
        saudacao = (f"Boa tarde {nome}!")
    else:
        saudacao = (f"Boa noite {nome}, agora são {hora_agora}:{minuto_agora}!")
    
    return render(request, "index.html", {'saudacao':saudacao})  """