# 54 - Crie um programa que leia o ano de nascimento de sete pessoas. No final,
# mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores. (Considere 21anos)

from datetime import date
anoatual = date.today().year
maioridade = 0
menor = 0
for c in range(1, 8):
    ano = int(input(f'Em que ano a {c} pessoa nasceu?: '))
    if anoatual - ano >= 21:
        maioridade += 1
    else:
        menor += 1
print('{} Pessoa não atingiram a maioridade ainda e {} já são maiores de 21.'.format(menor, maioridade))