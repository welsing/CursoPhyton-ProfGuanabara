# 087 - Aprimore o desafio anterior, mostrando no final:
# a) A soma de todos os valores PARES digitados.
# b) A soma dos valores da terceira coluna.
# c) O maior valor da segunda linha.

matriz = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
somaPar = somaTerceiraColuna = 0


for l in range(0,3):
    for c in range(0,3):
        while True:
            try:
                matriz[l][c] = int(input(f"Digite um número [{l+1}x{c+1}]: "))
                break
            except (ValueError):
                print('Digito invalido, tente novamente.')
        if matriz[l][c] % 2 == 0:
            somaPar += matriz[l][c]
        if c == 2:
            somaTerceiraColuna += matriz[l][c]
        if l == 1:
            if c == 0:
                maiorSegundaLinha = matriz[l][c]
            elif maiorSegundaLinha < matriz[l][c]:
                maiorSegundaLinha = matriz[l][c]
print('=-'*15)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end=' ')
    print()
print('-'*30)
print(f"A soma de todos os valores pares digitados é: {somaPar}")
print(f"A soma dos valores da 3º coluna: {somaTerceiraColuna}")
print(f"O maior valor da 2 linha é: {maiorSegundaLinha}")


