# 078 - Faça um programa que leia 5 VALORES NÚMERICOS e guarde-os em uma lista
# No final, mostrel qual foi o maior valor e o menor  valor digitados e suas respectivas posições na lista.

lista = []

for i in range(1, 6):
    n = int(input(f'Digite um valor para Posição {i}º: '))
    if i == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n
    lista.append(n)
print('='*25)
print(f'Você digitou os valores: {lista}')
print(f'O \033[34mmaior\033[m número é {maior} nas posições: ', end='')
for i, v in enumerate(lista):
    if v == maior:
        print(f'{i+1}... ', end='')
print('')
print(f'O \033[34mmenor\033[m número é o {menor} nas posições: ', end='')
for i, v in enumerate(lista):
    if v == menor:
        print(f'{i}... ', end='')
