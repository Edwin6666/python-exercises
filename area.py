#metodo para calcular area de un rectangulo
base=int(input("digite la base: "))
altura=int(input("digite la altura: "))


class rectangulo:

    def __init__ (self,base,altura):
        self.base=base
        self.altura=altura



    def area(self):
        return self.base * self.altura


rectangulo1=rectangulo(base,altura)

print(f'area del rectangulo: {rectangulo1.area()}')

