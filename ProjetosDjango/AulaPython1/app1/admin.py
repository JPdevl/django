from django.contrib import admin
from app1.models import Cliente, Produto, Pedido

admin.site.register(Cliente)
admin.site.register(Produto)
admin.site.register(Pedido)

# Register your models here.
