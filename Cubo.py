#calcular el volumen de un cubo
class cubo:

    def __init__(self, alto, ancho,profundidad):
        self.alto=alto
        self.ancho=ancho
        self.profundidad=profundidad


    def calcular_volumen_cubo(self):
        return self.alto * self.ancho * self.profundidad

alto=int(input('digite el alto: '))
ancho=int(input("Digite el ancho: "))
profundidad=int(input("digite la profundidad: "))


cubo1=cubo(alto,ancho,profundidad)

print(f'el volumen es: {cubo1.calcular_volumen_cubo()}')

