# 096 - Faça um programa que tenha uma função chamada area(), que receba as dimensões de um terreno retangular
# (largura e cumprimento) e mostre a area do terreno.

def area(larg, comp):
    calculo = larg * comp
    print(f'A area de {larg}m x {comp}m é {calculo}m².')


print('-\nCONTROLE DE TERRENOS\n-', '- '*15)
l = float(input('LARGURA (m): '))
print('-_'*8)
c = float(input('COMPRIMENTO (m): '))
area(l, c)