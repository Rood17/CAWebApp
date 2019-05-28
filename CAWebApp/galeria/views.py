from django.shortcuts import render, HttpResponse
from .models import imgGal
# Create your views here.
def test(request):
    gal = list(imgGal.objects.all())
    
    eventos = list(imgGal.objects.filter(presentacion__icontains='03'))
    escena = list(imgGal.objects.filter(presentacion__icontains='01'))
    espacios = list(imgGal.objects.filter(presentacion__icontains='02'))

    id_modal_escena = 12 + len(escena)
    id_modal_espacios = 8 + len(espacios) + id_modal_escena
    id_modal_eventos = len(eventos) + id_modal_espacios
    total_img = id_modal_eventos
    
    p = []
    aw = []
    for a in range(len(escena)):
        idd = {}
        idd['id'] = int(a + 1)
        p.append(idd)
        print(p)

    
        escenaa = [{'id':2, 'imagen':i.imagen.url, 'titulo':i.titulo}for i in escena]    
    
    
    print(aw)
    

   
#   'id_espacios':id_modal_espacios
    context = {'eventos':eventos, 'escena':escena}

    return render(request, 'galeria/galeria.html', context)