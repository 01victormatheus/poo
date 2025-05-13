class Contab():
    def __init__(self,numeroconta,saldo,nome,tipoconta):
        self.numeroconta=numeroconta
        self.status=True
        self.nome=nome
        self.tipoconta=tipoconta
        self.saldo=saldo
    def depositar(self,deposito):
            self.saldo=self.saldo+deposito
    def verificarsaldo(self):
        if self.status==True:
            print("conta ativa")
            print(self.saldo)
        else:
            print("conta inativa")
    def sacar(self,saque):
        if self.status==True:
            self.saldo-=saque
            print(f"seu saque foi de {saque} e seu saldo é de {self.saldo}")
        elif self.status==False:
                    print("conta inativa")
        else:
            print("sua conta está´inativa")
    def statuss(self):
        if self.status==True:
            print(f"sua conta está ativada")
        else:
            print("conta inativa")
    def ativar(self):
        if self.status==True:
            print("sua conta ja está ativa")
        else:
            self.status=True
            print("conta ativada com sucesso")
