class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f"Producto: {self.nombre} - Precio: ${self.precio}"


class Categoria:
    productos = []

    def __init__(self, nombre, productos):
        self.nombre = nombre
        self.productos = productos

    def agregar(self, producto):
        self.productos.append(producto)

    def imprimir(self):
        for producto in self.productos:
            print(producto)

    def __str__(self):
        return f"Categoria: {self.nombre} - Productos: {[str(p) for p in self.productos]}"


kayak = Producto("Kayak", 275)
bici = Producto("Bicicleta", 750)
surfboard = Producto("Surfboard", 500)

deportes = Categoria("Deportes", [kayak, bici])
deportes.agregar(surfboard)

deportes.imprimir()
