# 086 - Crie um programa que crie uma matriz de dimensões 3x3 e preencha os valores pelo teclado.
# No final, quero que me mostre a matrix na tela. Com a formatação correta.

matriz = [[], [], []]

for i in range(1,4):
    n = int(input(f'Insira um valor [1x{i}]: '))
    matriz[0].append(n)
for i in range(1,4):
    n = int(input(f'Insira um valor [2x{i}]: '))
    matriz[1].append(n)
for i in range(1,4):
    n = int(input(f'Insira um valor [3x{i}]: '))
    matriz[2].append(n)  
print('#'*20)

for i in range(0,3):
    print(f'[ {matriz[0][i]} ]', end=' ')
print()
for i in range(0,3):
    print(f'[ {matriz[1][i]} ]', end=' ')
print()
for i in range(0,3):
    print(f'[ {matriz[2][i]} ]', end=' ')