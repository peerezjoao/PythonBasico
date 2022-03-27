"""
Listas em Python
Fatiamento, append, insert, pop, del, clear, extend..
"""

# lista = ['a', 'b', 'c', 'd', 'e', 10.5]
# print(lista)
# print(lista[2])
# lista[2] = 'trocando o valor de uma lista'
# print(lista)
# print(lista[2])

# print(lista[-1])  # pegando último elemento da lista
# print(lista[0])   # pegando o primeiro elemento da lista
# print(lista[::2]) # step de 2 em 2
# print(lista[::-1]) # invertendo a lista



# l1 = [1,2,3]
# l2 = [4,5,6]
# l3 = l1 + l2  # fazendo a concatenação das listas
# l1.extend(l2) # adicionando os valores de l2
#l1.extend('adicionando um valor aleatório') # amplia a lista adicionando todos os itens do iterável.
                                            # ao invés de adicionar a String completa, adiciona de maneira fatiada.

# l2.append(10)  # adiciona o elemento sempre na última posição da lista
# l2.insert(0, 'banana') # adiciona o elemento na posição desejada
# print(l2)
# l2.pop()  # exclui o último valor da lista
# print(l2)

# print('Lista 4 ------------------- ')
# #     0,1,2,3,4,5,6,7,8     índices
# l4 = [1,2,3,4,5,6,7,8,9]
# l4.insert(0,'banana')
# print(l4)
# del(l4[0])
# print(l4)
#
# print('maior valor da lista: ' + str(max(l4)))
# print('menor valor da lista: ' + str(min(l4)))

# print('lista 5 *------------------*')
#
# soma = 0
# l5 = list(range(0,100,8))
# for i in l5:
#     soma = soma + i
# print(soma)
#
# print('Lista 6 *------------------*')
#
# l6 = ['String', True, 0, -20.5]
#
# for elemento in l6:
#     print(f'O tipo do elemento é {type(elemento)} e seu valor é {elemento}')

secreta = 'perfume'
dig = []
chances = 3

while True:
    if chances <= 0:
        print('Ops, parece que suas chances acabaram.')
        break

    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print('Por favor, digite apenas uma letra.')
        continue
    dig.append(letra)

    if letra in secreta:
        print(f'Oba! A letra {letra} pertence a palavra secreta.')
    else:
        print(f'Ops! A letra {letra} não pertence a palavra secreta.')
        dig.pop()

    secreto_temp = ''
    for letra_secreta in secreta:
        if letra_secreta in dig:
            secreto_temp += letra_secreta
        else:
            secreto_temp += '*'

    if secreto_temp == secreta:
        print(f'Parabéns, você descobriu a palavra secreta. A palavra secreta era {secreta}.')
        break
    else:
        print(f'A palavra secreta está assim: {secreto_temp}')

    if letra not in secreta:
        chances -= 1
    print(f'Você ainda tem {chances} chances')
    print()
