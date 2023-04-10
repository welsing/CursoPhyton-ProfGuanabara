# 065 - Crie um programa que leia vários números inteiros pelo teclado. 
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. 
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

n = 0
soma = 0
count = 0
resp = 's'

while resp not in 'Nn':
    n = int(input('Digite um número: '))
    soma += n
    if count == 0:
        menor = n
        maior = n
    if maior < n > menor :
        maior = n
    elif n < menor: 
        menor = n
    count += 1

    resp = input('Quer continuar? S/N: ').strip()[0]

media = soma/count
print(f'O maior número foi {maior} e o menor foi {menor}.')
print(f'A soma de todos so números digitados é {soma} e sua media é {media}')