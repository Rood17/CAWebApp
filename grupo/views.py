from django.shortcuts import render, HttpResponse
from .models import repertorio, propuesta, grupo
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404



# Create your views here.
def compañia(request):
    prop = propuesta.objects.all()
    rep = list(repertorio.objects.all())
    comp = list(grupo.objects.all())

    # Liliana Guido
    liliana = list(grupo.objects.filter(nombre__icontains='lili'))
    # Sandra
    sandra = list(grupo.objects.filter(nombre__icontains='sandra'))
    # William
    william = list(grupo.objects.filter(nombre__icontains='william'))
    # Alejandro
    alejandro = list(grupo.objects.filter(nombre__icontains='alejandro'))
    # Héctor
    hector = list(grupo.objects.filter(nombre__icontains='héctor'))

    print(rep)
    context = {'ale':alejandro,'hector':hector,'willi':william,
                'sandra':sandra,'lili':liliana,'propuesta':prop, 
                'repertorio':rep, 'comp':comp}
    return render(request, 'grupo/grupo.html', context)

def compañia_bio(request, act_id):
    actor = get_object_or_404(grupo, id=act_id)

    perfil = grupo.objects.filter(nombre__icontains=actor)
    context = {'perfil':perfil}
    print(str('Actor - ') + str(actor))

    return render(request, 'grupo/grupo_bio.html', context)