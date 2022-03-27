"""
Operadores lógicos
"""
# V e V = V
# V e F = F
# V or V = V
# V or F = V

usuario = input("nome de usuario: ")
senha = input("senha de acesso: ")

usuario_bd = 'joao'
senha_bd = '123'

if usuario == usuario_bd and senha == senha_bd:
    print("Carregando página de acesso, aguarde por gentileza.")
else:
    print("Usuário ou senha incorreto. Tente novamente!")