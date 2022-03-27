"""
Iniciar com letra, pode conter números, separar _ , letras minúsculas
"""

nome = "Joao Perez"
idade = 21
altura = 1.65
e_maior = idade > 18
peso = 62

print("Nome:", nome)
print("Idade:", idade)
print("altura:", altura)
print("Maior?:", e_maior)

print("*-----------Resolução do IMC------------------*")
imc = peso / (altura ** 2)
print(nome, " tem ", idade, " anos e seu IMC é: ", round(imc, 2))
