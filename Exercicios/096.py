# 096 - Faça um programa que tenha uma função chamada area(), que receba as dimensões de um terreno retangular
# (largura e cumprimento) e mostre a area do terreno.

def area(b, a):
    calculo = b * a
    print(f'A area de {b}m x {a}m é {calculo}m².')


print('   - CALCULADOR DE AREA EM METROS')
area(int(input('Digite largura: ')), int(input('Digite a altura: ')))