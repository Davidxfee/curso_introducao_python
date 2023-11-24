soma_idades = 0
contador = 0

while True:
    idade = int(input())
    if idade < 0:
        break

    soma_idades += idade
    contador += 1

if contador > 0:
    media_idades = soma_idades / contador
    print(f"{media_idades:.2f}")