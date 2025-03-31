from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request): # Nova Rota
    return render(request, 'home.html')
