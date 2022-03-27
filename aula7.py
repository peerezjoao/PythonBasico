nome = "Joao Perez"
idade = 21
altura = 1.65
e_maior = idade > 18
peso = 62
imc = peso / (altura ** 2)

print(f'{nome}, tem {idade} anos e seu IMC é {imc:.2f}')
print('{}, tem {} anos e seu IMC é {}'.format(nome,idade,imc))
print('{0}, tem {2} anos e seu IMC é {1}'.format(nome,idade,imc))
print('{n}, tem {i} anos e seu IMC é {im}'.format(n=nome,i=idade,im=imc))