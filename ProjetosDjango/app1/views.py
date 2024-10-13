from django.shortcuts import render
from datetime import datetime

# Create your views here.
def index_int(request, valor):
    return render(request, 'index.html', {'valor':valor, 'tipo': 'int'})

def index_str(request, valor):
    return render(request, 'index.html', {'valor':valor, 'tipo': 'str'})

def index_hora(request, nome):
    hora_agora = datetime.now().hour
    minuto_agora = datetime.now().minute

    if hora_agora > 5 and hora_agora < 12:
        saudacao = (f"Bom dia {nome}!")
    elif hora_agora > 12 and hora_agora < 18:
        saudacao = (f"Boa tarde {nome}!")
    else:
        saudacao = (f"Boa noite {nome}, agora são {hora_agora}:{minuto_agora}!")
    
    return render(request, "index.html", {'saudacao':saudacao})