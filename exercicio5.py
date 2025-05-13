class Animal():
    def __init__(self,nome,cor):
        self.nome=nome
        self.cor=cor
    def comer(self):
        print(f"o {self.nome} foi comer")
class Gato(Animal):
    def __init__(self,nome,cor):
        super().__init__(nome,cor)
    def miar(self):
        print(f"o {self.nome} está miando")
class Vaca(Animal):
    def __init__(self,nome,cor):
        super().__init__(nome,cor)
    def mugir(self):
        print(f"o {self.nome} está mugindo")
class Cachorro(Animal):
    def __init__(self,nome,cor):
        super().__init__(nome,cor)
    def latir(self):
        print(f"o {self.nome} está latindo")
class coelho(Animal):
    def __init__(self,nome,cor):
        super().__init__(nome,cor)
    def chiar(self):
        print(f"o {self.nome} está chiando")