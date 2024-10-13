from django.db import models

# Create your models here.

class Cliente(models.Model):
    nome = models.CharField(max_length=100, blank = False)
    cpf = models.CharField(max_length=11, blank = False)
    endereco = models.CharField(max_length=350, blank = False)
    data_nascimento = models.DateField(max_length=8)
    data_cadastro = models.DateTimeField(auto_now=True)
    data_ultima_alteracao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    cod = models.IntegerField(blank = False)
    nome = models.CharField(max_length=100, blank = False)
    valor_unitario = models.DecimalField(max_digits=7, decimal_places=2, blank = False)
      

    def __str__(self):
        return self.nome

class Pedido(models.Model):
    data = models.DateTimeField(auto_now=True)
    valor =  models.DecimalField(max_digits=6, decimal_places=2, blank = False)
    descricao = models.CharField(max_length=300, blank = False)
    id_cliente= models.ForeignKey(Cliente, on_delete=models.PROTECT)
    id_produto= models.ForeignKey(Produto, on_delete=models.PROTECT)  


