class Coordenadas:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

    # esto permite hacer la validación de igualdad entre objetos de la clase Coordenadas
    def __eq__(self, other):
        return self.lat == other.lat and self.lon == other.lon

    # esto permite hacer la validación de desigualdad entre objetos de la clase Coordenadas
    def __ne__(self, other):
        return self.lat != other.lat and self.lon != other.lon

    # esto permite hacer la validación de menor que entre objetos de la clase Coordenadas
    def __lt__(self, other):
        return self.lat + other.lat < self.lon + other.lon

    # esto permite hacer la validación de menor o igual que entre objetos de la clase Coordenadas
    def __le__(self, other):
        return self.lat + other.lat <= self.lon + other.lon


coords1 = Coordenadas(9, 20)
coords2 = Coordenadas(10, 20)

# False, porque son objetos diferentes en memoria (antes de implementar __eq__)
print(coords1 == coords2)
print(coords1 != coords2)
print(coords1 < coords2)
print(coords1 <= coords2)
