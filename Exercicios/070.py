# 070 - Crie um programa que leia o NOME e o PREÇO de varios produtos.
# O programa deverá perguntar se o usuario quer continuar ou não. No final, mostre:
# a) Qual é o total gasto na compra
# b) Quantos produtos custam mais de R$1000
# c) Qual é o nome do produto mais barato

from time import sleep
from os import system

# LIMPANDO A TELA
system('cls') or None

soma = mil_Produtos = count = preco = 0
mais_Barato = ''

print('#'*30)
print('{:-^30}'.format('CADASTRO DE PRODUTOS'))
print('#'*30)

while True:
    nome = input('NOME: ').strip()
    preco = float(input('PREÇO R$: '))
    soma += preco
    if count == 0 or preco < mais_Barato:
        preco_Barato = preco
        mais_Barato = nome
  # if preco < preco_Barato:
    #   preco_Barato = preco
    #   mais_Barato = nome

    if preco > 1000:
        mil_Produtos += 1

    count += 1

    while True:
        continuar = input('Quer continuar?[S/N]: ').strip().upper()[0]
        if continuar in 'SN':
            print('-'*30)
            break
        else:
            print("RESPOSTA INVALIDA! Tente novamente...")
    if continuar == "N":
        print('CALCULANDO...')
        sleep(2)
        system('cls')
        break

print(f'O produto mais barato foi {mais_Barato} por R${preco_Barato}.')
print(f'{mil_Produtos} produtos mais caros que R$1000')
print(f'TOTAL GASTO: R${soma:.2f}')


print('FIM!')
