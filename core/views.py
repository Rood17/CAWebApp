from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return render(request, 'core/index.html')

def base(request):
    return render(request, 'core/base.html')

def foro(request):
    return render(request, 'core/foro.html')

def convocatorias(request):
    return render(request, 'core/convocatorias.html')

def rentas(request):
    return render(request, 'core/rentas.html')
