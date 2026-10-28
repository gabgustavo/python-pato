from .models import Categoria, Producto
from django.contrib import admin


# con la siguiente clase se pueden definir los campos visibles en la administración
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')


class ProductoAdmin(admin.ModelAdmin):
    # campos que se visualizaran o no en el formulario
    # fields = ()
    exclude = ('creado_en', )
    list_display = ('id', 'nombre', 'stock', 'creado_en')

# Register your models here.


admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Producto, ProductoAdmin)
