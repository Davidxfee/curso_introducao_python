while True:
    # Leitura dos valores X e Y
    x, y = map(int, input().split())

    # Verifica se os valores são iguais, encerrando o loop se forem
    if x == y:
        break

    # Verifica a ordem e imprime a mensagem correspondente
    if x < y:
        print("Crescente")
    else:
        print("Decrescente")