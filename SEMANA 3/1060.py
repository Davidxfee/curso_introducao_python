contador = 0
for i in range(1, 7):
    valor = float(input())
    if valor > 0:
        contador += 1
print(f"{contador} valores positivos")