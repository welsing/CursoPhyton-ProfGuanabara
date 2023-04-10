# 059 - Crie um programa que leia dois valores e mostre um menu na tela:
# [1] Somar
# [2] Multiplicar
# [3] Maior
# [4] Novos Números
# [5] Sair do programa
# Seu programa deverá realizar a operação solicitada em casa caso.
from time import sleep
import os
print("{:^50}".format('\033[7m___MENU CALCULATOR___\033[m'))
print('-='*10)
n1 = int(input('Digite o 1º valor: '))
print('-='*10)
n2 = int(input('Digite o 2º valor: '))
print('-='*10)

opcao = 0
while opcao != 5:
    print(''' 🤖 O QUE DESEJA \033[4mFAZER\033[m?
    [1] - Somar ➕
    [2] - Multiplicar 🎲
    [3] - Maior 🎭
    [4] - Add novos números 🧩
    [5] - SAIR ❌
    ''')
    opcao = input('>>>>> Escolha uma opção: ')
    opcao = int(opcao)
    os.system('cls')
    if opcao == 1:
        print('SOMANDO...')
        sleep(1)
        print(f'A soma de {n1} + {n2} é {n1 + n2}')
    elif opcao == 2:
        print('CONSULTANDO TABUADA...')
        sleep(1)
        print(f'O produto de {n1} x {n2} é {n1*n2}')
    elif opcao == 3:
        print('ANALISANDO...')
        sleep(1)
        if n1 > n2:
            print(f'O número {n1} é maior que {n2}!')
        elif n2 > n1:
            print(f'O número {n2} é maior que {n1}!')
        else: 
            print('Os dois números são iguais!')
    elif opcao == 4:
        print('-='*10)
        n1 = int(input('Digite o novo 1º valor: '))
        print('-='*10)
        n2 = int(input('Digite o novo 2º valor: '))
        print('-='*10)
    elif opcao != 5:
        print('OPÇÃO \033[31mINVALIDA\033[m, TENTE NOVAMENTE!')
    print('LOADING...')
    sleep(2)
    
    
print('ATÉ LOGO! 👋')