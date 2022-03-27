"""
Formatação de Strings

:S - texto (strings)
:d - inteiros (int)
:f - números de ponto flutuante (float)
:.(número)f - quantidade de casas decimais (float)
:(caracter) (> ou < ou ^)(quantidade)(tipos - s,d ou f)

< - esquerda
> - direita
^ - centro
"""
num1 = 1
print(f'{num1:0<10}')

num2 = 1150
print(f'{num2:0>10}')

num3 = 50
print(f'{num3:0^15}')

nome = 'João'
sobrenome = 'Perez'
print(f'{nome:#^10}')

nome_formatado = '{0:#>10} {1:@<20}'.format(nome, sobrenome)  # preenche o restante de caracteres até chegar a 50.
print(nome_formatado)

print(nome.lower())
print(nome.upper())
print(nome.title())
