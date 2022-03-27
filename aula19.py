"""
For in
Iterando Strings com For

Função range( start=0, stop, step =1 )
"""

text = 'Python'
nova_string = ''
for letra in text:
    if letra =='t':
        nova_string = nova_string + letra.upper()
    elif letra == 'h':
        nova_string += letra.upper()
        break
    else:
        nova_string += letra

print(nova_string)

# for numero in range(0, 100, 8):
#     print(numero)
#
# for n in range(100):
#     if n % 8 == 0:
#         print(n)