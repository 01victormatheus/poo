class Forma():
    def __init__(self):
        self.area=0
        self.perimetro=0
class Retangulo(Forma):
    def __init__(self,altura,base):
        super().__init__()
        self.altura=altura
        self.base=base

    def CalcularArea(self):
        self.area=(self.base*self.altura)
        print(self.area)
    def calculaperimetro(self):
        self.perimetro=2*(self.base+self.altura)
        print(self.perimetro)

class Triangulo(Forma):
    def __init__(self,base,altura):
        super().__init__()
        self.base=base
        self.altura=altura
    def calcularArea(self):
        self.area=(self.base*self.altura)/2
        print(self.area)
    def calculaperimetro(self):
        self.area=(self.base*self.altura)/2
        self.perimetro=self.area=self.base+self.altura
        print(self.perimetro)





