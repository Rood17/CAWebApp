from django.shortcuts import render, HttpResponse
from .models import grupoForo, Colaborador
from django.contrib.auth.models import User



# Create your views here.
def perfiles(request):
    test = list(grupoForo.objects.all())
    context = {'all':test}
    return render(request, 'about/about.html', context)

def AboutBio(request, colaborador_id):
    col = User.objects.filter (id=colaborador_id)

    for i in col:
        a = i.first_name

    perfil = grupoForo.objects.filter(nombre__first_name=a)
    context = {'perfil':perfil}

    return render(request, 'about/about-bio.html', context)