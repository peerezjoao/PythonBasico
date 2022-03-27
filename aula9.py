"""
Condições IF, ELIF e ELSE
"""
#
# if True:
#     print("Verdade.")
# else:
#     print("Falso.")



#Operadores lógicos     == igualdade
#  >= maior/igual que     =< menor/igual que
# != diferente

# num_1 = 2
# num_2 = 3
# expressao = (num_1 <= num_2)
#
# print(expressao)

nome = input("Qual seu nome? ")
idade = int(input("Qual sua idade? "))

idade_menor = 20
idade_maior = 30

if idade >= idade_menor and idade <= idade_maior:
    print(f'{nome}, pode pegar o empréstimo')
else:
    print(f'{nome}, o seu empréstimo não esta dísponivel')





