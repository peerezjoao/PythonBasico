"""
* criar variáveis para nome, idade
  altura e peso de uma pessoa.
* criar a variável com o ano atual
* obter o ano de nascimento da pessoa
* obter o IMC da pessoa com 2 casas decimais
* Exibir um texto com todos os valores usando f''
"""
nome = 'João Perez'
ano_atual = 2021
idade = 21
ano_nascimento = ano_atual - idade
altura = 1.65
peso = 60
imc = peso / (altura**2)

print(f'{nome}, tem {idade} anos, {altura} de altura e pesa {peso}kg.')
print(f'O IMC de {nome} é {imc:.2f}')
print(f'{nome} nasceu no ano de {ano_nascimento}')
