from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


# link: /products
def index(request):
    return HttpResponse('Mensaje de bienvenida')
