from django.shortcuts import render, HttpResponse
from .models import preguntas

# Create your views here.
def test(request):
    todas = list(preguntas.objects.all())

    context = {'faqs':todas}

    return render(request, 'faqs/faqs.html', context)