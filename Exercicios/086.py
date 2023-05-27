# 086 - Crie um programa que crie uma matriz de dimensões 3x3 e preencha os valores pelo teclado.
# No final, quero que me mostre a matrix na tela. Com a formatação correta.

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite o valor [{l+1}x{c+1}]: '))
for l in range(0, 3):
    for c in range(0, 3):
        print(f"[{matriz[l][c]:^5}]", end=' ')
    print()


