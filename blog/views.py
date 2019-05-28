from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import entradaBlog, etiquetasBlog, CategoryBlog,CategoryStudyBlog

# Create your views here.
def test(request):
    allEntradas = entradaBlog.objects.filter(donativo__icontains='01')  
    cMain = allEntradas.filter(categoria__icontains='02')[:1]
    cSec = allEntradas.filter(categoria__icontains='01')[:1]
    cTer = allEntradas.filter(categoria__icontains='03')[:1]
    cCuart = allEntradas.filter(categoria__icontains='04')[:1]
    cQuint = allEntradas.filter(categoria__icontains='05')[:1]
    etq = [] 
     
     
     # Lista de etiquetas (filtros)
    for i in allEntradas:
        for a in i.etiquetaBlog.all():
            x = a.name
            etq.append(x)
    
    etiquetas = list(set(etq))

    
    # Primero jalar todas las etiquetas
    # ordenarlas y que no se repitan
    # imprimirlas en un query
    context = {'test':allEntradas, 'cMain':cMain, 'cSec':cSec, 
                'cTer':cTer, 'cCuart':cCuart, 'cQuint':cQuint,
                'etiquetas':etiquetas}

    return render(request, 'blog/blog.html', context)

def Categorias(request, category_id):

    # Filtros
    allEntradas = entradaBlog.objects.filter(donativo__icontains='01')  
    cMain = allEntradas.filter(categoria__icontains='02')[:1]
    cSec = allEntradas.filter(categoria__icontains='01')[:1]
    cTer = allEntradas.filter(categoria__icontains='03')[:1]
    cCuart = allEntradas.filter(categoria__icontains='04')[:1]
    cQuint = allEntradas.filter(categoria__icontains='05')[:1]
    etq = [] 
     
     
     # Lista de etiquetas (filtros)
    for i in allEntradas:
        for a in i.etiquetaBlog.all():
            x = a.name
            etq.append(x)
    
    etiquetas = list(set(etq))

    # Queries
    if 'reseñas' in category_id:
        catB = '02'
    if 'articulos' in category_id:
        catB = '01'
    if 'entrevistas' in category_id:
        catB = '03'
    if 'enprofundidad' in category_id:
        catB = '04'
    if 'noticias' in category_id:
        catB = '05'

   
        
    post = entradaBlog.objects.filter(categoria__icontains=catB)
    

    context = {'test':allEntradas, 'cMain':cMain, 'cSec':cSec, 
                'cTer':cTer, 'cCuart':cCuart, 'cQuint':cQuint,
                'post':post, 'etiquetas':etiquetas}

    return render(request, 'blog/blog_category.html', context)
