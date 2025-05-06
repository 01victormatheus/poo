from exercicio1 import Pessoa
aluno01 = Pessoa("guilherme",21,82)
aluno02=Pessoa("victor",20,76)
print(f"{aluno01.nome} tem {aluno01.idade} anos e pesa {aluno01.peso}kg")
print(f"{aluno02.nome} tem {aluno02.idade} anos e pesa {aluno02.peso}kg")



aluno02.falar()
aluno02.comer("pipoca")
aluno02.dormir()