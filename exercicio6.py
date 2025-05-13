class Ingresso():
    def __init__(self,valor):
        self.valor=valor
    def imprimeValor(self):
        print(f"o ingresso custa {self.valor}")
class IngVip(Ingresso):
    def __init__(self,valor):
        super().__init__(valor)
        self.valor += (self.valor * 50 / 100)
    def MostrarVip(self):
        print(f"o valor do ingresso custou {self.valor}")
a=IngVip(100)
a.MostrarVip()
