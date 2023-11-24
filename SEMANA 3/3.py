N = int(input())
if 2 < N < 1000:
    for i in range(1, 11):
        resultado = i * N
        print(f"{i} x {N} = {resultado}")
else:
    print("Valor de N fora do intervalo permitido.")