from django.shortcuts import render, HttpResponse

# Create your views here.

def historia(request):
    return render(request, 'historia/historia.html')