#Linea
class Punto:
    def __init__(slef, x, y):
        slef.x = x
        slef.y = y

    def __str__(self):
        return ("{}, {}").format(self.x, self.y)


class Linea:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __str__(self):
        return ("{}, {}").format(self.p1, self.p2)

    def dibujarLinea(self):
        print("dibujar Linea", self)


if __name__ == "__main__":
    punto1 = Punto(0, 0)
    punto2 = Punto(5, 5)
    linea = Linea(punto1, punto2)

    print(linea)
    linea.dibujarLinea()

#Circulo
class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "{}, {}".format(self.x, self.y)

class Circulo:
    def __init__(self, centro, radio):
        self.centro = centro
        self.radio = radio

    def __str__(self):
        return "Circulo({}, {}, radio={})".format(self.centro.x, self.centro.y, self.radio)

    def dibuja_circulo(self):
        print("Dibujando un círculo en {} con radio {}".format(self.centro, self.radio))

centro = Punto(5, 10)
circulo = Circulo(centro, 3.5)
print(circulo)
circulo.dibuja_circulo()

