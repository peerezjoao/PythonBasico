"""
Desempacotamento de Listas
"""

lista = ['Joao', 'Luiz', 'Maria', 1,2,3,4,5]

n1, n2, *outra_lista, ultimo_lista = lista   # (*) gera uma outra lista com o restante dos valores. resto de valores
print(n1)
print(n2)
print(*outra_lista)
print(ultimo_lista)

n1, *_ = lista
print(n1)
