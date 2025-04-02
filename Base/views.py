from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from Base import models
from Base.models import Contact
# Create your views here.



def contact(request):
    if request.method == "POST":
        print("post")
        name = request.POST.get("Nome")  # campos do html
        email = request.POST.get("Email")  
        content = request.POST.get("Content")
        print(name, email, content)

        if len(name) > 1 and len(name) < 30:
            pass
        else:
            messages.error(request, "Nome deve possuir mais de 2 e menos de 30 caracteres.")
            return render(request, "home.html")
        
        if len(email) > 1 and len(email) < 30:
            pass
        else:
            messages.error(request, "Email inválido.")
            return render(request, "home.html")
        
        # Salvar os dados
        ins = models.Contact(name=name, email=email, content=content)
        ins.save()
        messages.success(request, "Mensagem enviada com sucesso!")
        print("Data has been saved into the database")
    
    return render(request, "home.html")