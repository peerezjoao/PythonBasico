# Faça um programa que peça ao usuário para digitar um número inteiro, informe se este número é par ou ímpar.
# Caso o usuário não digite um número inteiro, informe que não é um número inteiro.

num1 = input("Digite um número: ")
if num1.isnumeric():
    resto = int(num1) % 2
    if resto == 0:
        print(f"O número digitado foi {num1}, e ele é par.")
    else:
        print(f"O número digitado foi {num1}, e ele é ímpar.")
else:
    print('A entrada de dado não foi um número inteiro.')


# Faça um programa que pergunte a hora ao usuário, baseando-se no horário descrito, exiba a saudação apropriada.
# bom dia 0-11, boa tarde 12-17 e boa noite 18-23.

hora = input('Qual a hora atual, sem minutos: ')
nome_hora = input('Digite seu nome, por gentileza: ')

if hora.isnumeric():
    hora = int(hora)
    if hora < 0 or hora > 23:
        print("Horário deve estar entre 0 e 23.")
    else:
        if hora >= 0 and hora <= 11:
            print(f"Bom dia, {nome_hora}")
        elif hora >= 12 and hora <= 17:
            print(f"Boa tarde, {nome_hora} ")
        else:
            print(f"Boa noite, {nome_hora}")

# Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou menos escreva
# Seu nome é curto; se tiver entre 5 e 6 letras, escreva Seu nome é normal; maior que 6, escreva Seu nome é grande

nome = input("Digite o seu nome, por gentileza: ")
tamanho_nome = len(nome)

if tamanho_nome <= 4:
    print(f"Seu nome é curto, possui apenas {tamanho_nome} caracteres.")
elif tamanho_nome >= 5 and tamanho_nome <= 6:
    print(f'Seu nome é normal, possui apenas {tamanho_nome} caracteres. ')
else:
    print(f'Seu nome é grande, possui apenas {tamanho_nome} caracteres. ')
