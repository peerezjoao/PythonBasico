"""
For / else
"""

lista = ['Pedro', 'Paula', 'Joao', 'Marcos Pequin']
comeca_com_j = False

for nome in lista:
    if nome.lower().startswith('j'):
        continue
    print(nome)

# geralmente não seu usa For / Else, mas todavia, existe como usar
# While / Else e For / Else