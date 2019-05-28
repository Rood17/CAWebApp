from .models import Link

def ctx_dict(request):
    ctx = {}
    links = Link.objects.all()

    for i in links:
        ctx[i.key] = i.url

    return ctx