"""
Operação ternária
"""

# logged_user = False
# msg = "Usuário logado." if logged_user else "Usuário precisa logar."
#
# print(msg)

idade = input("Qual sua idade? ")

if not idade.isnumeric():
    print("Você precisa digitar apenas números.")
else:
    maior_idade = int(idade) >= 18
    msg = "Pode acessar sistema" if maior_idade else "Não pode acessar esse sistema"

    print(msg)