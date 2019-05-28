from django.shortcuts import render, HttpResponse
from .models import repertorio, propuesta, grupo
# Create your views here.
def compañia(request):
    prop = list(propuesta.objects.all())
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
    context = {'ale':alejandro,'hector':hector,'willi':william,'sandra':sandra,'lili':liliana,'propuesta':prop, 'repertorio':rep, 'comp':comp}
    return render(request, 'grupo/grupo.html', context)