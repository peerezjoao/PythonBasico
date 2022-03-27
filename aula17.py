"""
While / Else
contadores
acumuladores
"""

contador = 1
acumulador = 1

while contador <= 10:
    print(contador)

    acumulador = acumulador + contador
    contador += 1

    print(f"Acumulador: {acumulador}")
else:
    print("Tentativa de Login excedida.")