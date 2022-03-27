"""
Split, Join, Enumarate ( para objetos iteráveis )
"""


# split
#
# string = 'O Brasil país do futebol, o Brasil é o penta.'
#
# lista1 = string.split(' ')
# lista2 = string.split(',')
# palavra = ''
# contagem = 0
# for indices in lista1:
#     qtd_vezes = lista1.count(indices)
#
#     if qtd_vezes > contagem:
#         contagem = qtd_vezes
#         palavra = indices
#
# print(f' a palavra que apareceu mais vezes é {palavra} {(contagem)}x')
# for valor in lista2:
#     print(valor.strip().capitalize())

string = 'O Brasil é penta.'
lista = string.split(' ')
# string2 = ','.join(lista)
# print(string)
# print(lista)
# print(string2)

# for indice, valor in enumerate(lista):
#     print(indice, valor, lista[indice])

lista2 = [
    [0,'Luiz'],
    [1,'Joao'],
    [2,'Maria']
]
for v in lista2:
    print(v)
    print(v[0], v[1])

for valor in enumerate(lista2):   # desempacotamento dos elementos dentro da lista
    print(valor)


# função enumerate faz com tuplas


n1, n2, n3 = lista2
print(n1)
print(n2)
print(n3)





