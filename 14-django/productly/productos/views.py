from django.http import Http404, HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404

from .models import Producto

# Create your views here.


# link: host/products
def index(request):
    # productos = Producto.objects.all()
    productos = Producto.objects.all()
    # productos = Producto.objects.filter(puntuaje=5)
    # productos = Producto.objects.filter(puntuaje__gte=3)
    # productos = Producto.objects.get(id=1)
    # productos = Producto.objects.get(pk=1)
    # print(productos)
    # return HttpResponse(productos[0].nombre)
    # return JsonResponse(list(productos), safe=False)

    return render(
        request,
        'index.html',
        context={'productos': productos}
    )


def detail(request, producto_id):
    try:
        producto = Producto.objects.get(id=producto_id)
        # producto = get_object_or_404(Producto, id=producto_id)

        return render(
            request,
            'detail.html',
            context={'producto': producto}
        )
    except Producto.DoesNotExist:
        #    raise Http404()
        return render(
            request,
            '404.html'
        )
