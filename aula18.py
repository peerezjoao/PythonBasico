# índices == valores iteravéis

frase = 'o rato roeu a roupa do rei de roma'
tamanho_frase = len(frase)
contador = 0
nova_string = ''

input_do_usuario = input("Digite uma letra para colocar em maisculo: ")

# iteração
while contador < tamanho_frase:
    #print(frase[contador], contador)
    letra = frase[contador]
    if letra == input_do_usuario:
        nova_string += input_do_usuario.upper()
    else:
        nova_string += letra
    contador += 1
print(nova_string)

# while contador < 10:
#     print(contador)
#     contador += 1
