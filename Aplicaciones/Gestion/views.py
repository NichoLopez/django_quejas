
from django.http import HttpRequest
from django.shortcuts import render
from Gestion.forms import FormularioQueja

# Create your views here.

class FormularioQuejaView(HttpRequest):

    def index(request):
        queja = FormularioQueja()
        return render(request, "QuejaIndex.html", {"form":queja})
    
    def procesar_formulario(request):
        queja = FormularioQueja(request.POST)
        if queja.is_valid():
            queja.save()
            queja = FormularioQueja()

        return render(request, "QuejaIndex.html", {"form":queja, "mensaje":'OK'})
