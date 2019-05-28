from django.shortcuts import render, get_object_or_404, render_to_response
from .models import Book, CategoryStudyBiblio, etiquetasBiblio
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Default Lista
def biblioteca(request):
    
    return render(request, 'biblioteca/biblioteca.html')

def biblioIndex(request):
    lista = Book.objects.all()
    libros = Book.objects.all().order_by('-created')
    cates = CategoryStudyBiblio.objects.all()
    query = request.GET.get('qs', None)
    listaResul = Book.objects.search(query)
    
    print('QUERYYYYY')
    print(query)
    print(listaResul)
    # Filtros Lista
    if 'title' in request.GET:
        lista = Book.objects.all().order_by('titulo')

    if 'author' in request.GET:
        lista = Book.objects.all().order_by('autor')

    if 'year' in request.GET:
        lista = Book.objects.all().order_by('year')
    
    # Pagination
    paginator = Paginator(lista, 3)
    page = request.GET.get('page')
    lista = paginator.get_page(page)

    # Safe filter paginator
    get_dict_copy = request.GET.copy()
    params = get_dict_copy.pop('page', True) and get_dict_copy.urlencode()



    # Diccionarios
    context = {'cates':cates ,'lista':lista, 'libros':libros , 
                'params':params, 'listaResul':listaResul, 'query':query}
    return render(request, 'biblioteca/biblio-index.html', context)

    # Categorias de estudio
def categoria_estudio(request, cate_id):
    cate = get_object_or_404(CategoryStudyBiblio, id=cate_id)
    lista = Book.objects.filter(categorias__cat_estudio=cate).distinct()
    
    listaa = etiquetasBiblio.objects.filter(cat_estudio=cate).distinct()

    # Pagination
    paginator = Paginator(lista, 3)
    page = request.GET.get('page')
    lista = paginator.get_page(page)

    # Safe filter paginator
    get_dict_copy = request.GET.copy()
    params = get_dict_copy.pop('page', True) and get_dict_copy.urlencode()


    context = {'cate':cate,'listaa':listaa, 'lista':lista, 'params':params}
    return render(request, "biblioteca/biblio_cat_estudio.html", context)

    # Etiquetas 
def etqtBiblio(request, etiqueta_id):
    etqt = get_object_or_404(etiquetasBiblio, id=etiqueta_id)
    lista = Book.objects.filter(categorias=etiqueta_id).distinct()

    # Pagination
    paginator = Paginator(lista, 3)
    page = request.GET.get('page')
    lista = paginator.get_page(page)

    # Safe filter paginator
    get_dict_copy = request.GET.copy()
    params = get_dict_copy.pop('page', True) and get_dict_copy.urlencode()

    context = {'lista':lista, 'etiqueta':etqt, 'params':params}
    return render(request, "biblioteca/biblio_etiquetas.html", context)
