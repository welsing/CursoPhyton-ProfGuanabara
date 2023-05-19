# 087 - Aprimore o desafio anterior, mostrando no final:
# a) A soma de todos os valores PARES digitados.
# b) A soma dos valores da terceira coluna.
# c) O maior valor da segunda linha.

matriz = [[], [], []]
soma_Pares = 0

for i in range(1,4):
    n = int(input(f'Digite um valor [1x{i}]:'))
    if n % 2 == 0:
        soma_Pares += n
    if i == 2:
        maior_Segunda_Coluna = n
    matriz[0].append(n)
for i in range(1,4):
    n = int(input(f'Digite um valor [2x{i}]:'))
    if n % 2 == 0:
        soma_Pares += n
    if i == 2 and maior_Segunda_Coluna < n:
        maior_Segunda_Coluna = n
    matriz[1].append(n)
for i in range(1,4):
    n = int(input(f'Digite um valor [3x{i}]:'))
    if n % 2 == 0:
        soma_Pares += n
    if i == 2 and maior_Segunda_Coluna < n:
        maior_Segunda_Coluna = n
    matriz[2].append(n)

print('#'*30)

for i in range(0,3):
    print(f'[ {matriz[0][i]} ]', end=' ')
print()
for i in range(0,3):
    print(f'[ {matriz[1][i]} ]', end=' ')
print()
for i in range(0,3):
    print(f'[ {matriz[2][i]} ]', end=' ')
print()

print(f'A soma de todos os valores pares é {soma_Pares}')
print('A soma dos valores da 3º coluna: {}'.format(matriz[0][2] + matriz[1][2] + matriz[2][2]))
print(f'O maior valor da 2º coluna: {maior_Segunda_Coluna}')