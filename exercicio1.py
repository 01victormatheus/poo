class Pessoa():
    def __init__(self, nome,idade,peso):
        self.nome=nome
        self.idade=idade
        self.peso=peso
        self.comendo=False
        self.dormindo=False
        self.falando=False
    def falar(self):
        if self.falando==True:
            print("imbecíl,ja esta´falando")
        print(f"{self.nome} começou a falar")
    def comer(self, comida):
        print(f"{self.nome} acabou de comer {comida} ")
    def dormir(self):
        print(f"{self.nome} agora vai dormir")



