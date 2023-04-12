
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def aplica_compras(request):
    return render(request, "aplica_compras.html")