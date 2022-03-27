usuario = input("digite seu nome de usuário: ")
qtd_caracter = len(usuario)

# print(f'{usuario}, {qtd_caracter}', type(qtd_caracter))

if qtd_caracter < 6:
    print("Você precisa digitar pelo menos 6 caracteres!")
else:
    print("Cadastro realizado com sucesso.")

