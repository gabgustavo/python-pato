from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

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
