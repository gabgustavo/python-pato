def getProduct(**datos):
    print(datos)
    formatted = f"\nID: {datos['id']}, Titulo: {datos['name']}, Precio: {datos['price']}, Cantidad: {datos['stock']}"
    print(formatted)


getProduct(id=1, name="Laptop", price=1500, stock=30)
