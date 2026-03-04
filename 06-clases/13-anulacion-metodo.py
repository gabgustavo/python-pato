# clase padre
class Ave:
    def __init__(self):
        self.volador = True

    def vuela(self):
        print("vuela ave")


# clase hija (subclase)
class Pato(Ave):
    def __init__(self):
        super().__init__()  # llama al constructor de la clase padre (Ave)
        self.nada = True

    def vuela(self):
        super().vuela()  # llama al método vuela de la clase padre (Ave)
        print("vuela pato")


pato = Pato()
pato.volador()
