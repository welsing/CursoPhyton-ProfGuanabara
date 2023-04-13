# 069 - Crie um programa que leia a IDADE e o SEXO de varias pessoas. 
# A cada pessoa cadastrada o programa deverá perguntar se o usuario quer continuar ou não. No final, mostra:
# a) Quantas pessoas tem mais de 18 anos.
# b) Foram cadastrados quantas mulheres.
# c) Quantas mulheres tem menos de 20 anos.

import os
from time import sleep


os.system('cls')
print('#'*30)
print('{:^30}'.format('CADASTRO DE PESSOA'))
print('#'*30)

maior_Idade = count_F = count_F_Idade = 0

while True:
    idade = int(input('IDADE: '))
    sexo = input('SEXO [F/M]: ').strip().upper()[0]

    if idade > 18:
        maior_Idade += 1
    
    if sexo == 'F':
        count_F += 1
        if idade < 20:
            count_F_Idade += 1

    # QUER CONTINUAR?
    while True:
        continuar = input('Quer continuar? [S/N]: ').upper().strip()[0]
        if continuar in 'SN':
            print('-='*20)
            break
        else:
            print('RESPOSTA INVALIDA! Tente novamente.')
    if continuar == 'N':
        print('ANALISANDO...')
        sleep(1)
        print('CRIANDO TABELA...')
        sleep(2)
        os.system('cls')
        break


print('='*40)
print('{:^40}'.format('ANALISE DE DADOS'))
print('='*40)
print(''' PESSOAS +18 | MULHERES | MULHERES -20
        {}    |    {}     |    {}
'''.format(maior_Idade, count_F, count_F_Idade))


print('FIM!')