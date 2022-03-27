"""
Desafio contadores paralelos
"""
x = 0
y = 10
while x <= 10 and y > 0:
    y -= 1
    x += 1
    print(x, y)

# outra solução
for p, r in enumerate(range(10, 1, -1)):
    print(p, r)
