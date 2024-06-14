from django.shortcuts import render

# Create your views here.

def home(request):
    # Renderiza la plantilla 'index.html' y la devuelve como respuesta
    return render(request, 'index.html') 