class Atleta():
    def __init__(self,aposentado,peso):
        self.aposentado=False
        self.peso=peso
        self.aquecer=False
    def Aposentar(self):
        if self.aposentado ==True:
            print(f"este atleta está aposentado")
        else:
            self.aposentado=True
            print("o atleta acabou de se aposentar")
    def Aquecer(self):
        if self.aposentado==False:
            self.aquecer=True
            print("atleta apto e aquecido")
        




