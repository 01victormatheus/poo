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
            print(f"{self.nome} começou a falar")
        else:
            if self.comendo==True:
                print("ele não pode falar ,porque está comendo")
            else:
                if self.dormindo==True:
                    print("ele não pode falar dormindo")
                else:
                    if self.falando==False:
                        print("ele não está falando,deve está fazendo outra")
                        self.falando==True
    def comer(self, comida):
        if self.comendo==True:
            print(f"{self.nome} acabou de comer")
        else:
            if self.falar==True:
                print("ele não pode comer,pos ele está falando")
            else:
                if self.dormindo == True:
                        print("ele não pode comer dormindo")
                else:
                    if self.comendo == False:
                        print("ele não está comendo,deve está fazendo outra")
                        self.comendo == True

    def dormir(self):
        if self.dormindo==True:
            print(f"{self.nome} está dormindo")
        else:
                if self.falar == True:
                    print("ele não pode dormir,pos ele está falando")
                else:
                    if self.comendo == True:
                        print("ele não pode dormir comendo")
                    else:
                     if self.dormindo == False:
                        print("ele começou a dormir")
                        self.dormindo == True
    def acordar(self):
        if self.dormindo==True:
           self.dormindo=False
           print("acorda mermão")

        else:
                print("ele acordou")
    def pararcomer(self):
        if self.comendo==True:
           self.comendo=False
           print("parou de comer")
        else:
            print("ja está comendo")


