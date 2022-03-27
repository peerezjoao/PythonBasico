"""
Laço While
"""

# contador = 0
#
# while contador <= 10:
#     # continue - pula para o próximo laço ou não continua as linhas
#     if contador == 3:
#         contador += 1
#         continue
#
#     print(contador)
#     contador = contador + 1


# x = 0
# while x < 10:
#     y = 0
#     while y < 5:
#         print(f'({x}), ({y})')
#         y += 1
#     x += 1
#
# print('Acabou.')


while True:
    print()
    num1 = input('Digite um número: ')
    num2 = input('Digite outro número: ')
    operador = input('Digite um operador: ')
    sair = input('Deseja sair? [s]im ou [n]ão? ')

    if sair == 's':
        break

    if not num1.isnumeric() or not num2.isnumeric():
        print('Você precisa digitar um número ou "sair"')
        continue

    num1 = int(num1)
    num2 = int(num2)

    if operador == '+':
        print(num1 + num2)

    elif operador == '-':
        print(num1 - num2)

    elif operador == '/':
        print(num1 / num2)

    elif operador == '*':
        print(num1 * num2)

    else:
        print('Operador inválido!')

