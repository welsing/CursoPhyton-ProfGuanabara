# 069 - Crie um programa que leia a IDADE e o SEXO de varias pessoas. 
# A cada pessoa cadastrada o programa deverá perguntar se o usuario quer continuar ou não. No final, mostra:
# a) Quantas pessoas tem mais de 18 anos.
# b) Foram cadastrados quantas HOMENS.
# c) Quantas mulheres tem menos de 20 anos.

import os
from time import sleep


os.system('cls')
print('#'*30)
print('{:^30}'.format('CADASTRO DE PESSOA'))
print('#'*30)

maior_Idade = count_M = count_F_Idade = 0

while True:
    idade = int(input('\033[34mIDADE\033[m: '))
    sexo = input('\033[34mSEXO\033[m [F/M]: ').strip().upper()[0]

    if idade > 18:
        maior_Idade += 1
    
    if sexo == 'M':
        count_M += 1

    if sexo == 'F' and idade < 20:
        count_F_Idade += 1

    # QUER CONTINUAR?
    while True:
        continuar = input('\033[33mQuer continuar?\033[m [\033[32mS\033[m/\033[31mN\033[m]: ').upper().strip()[0]
        if continuar in 'SN':
            print('-='*20)
            break
        else:
            print('RESPOSTA \033[31mINVALIDA\033[m! Tente novamente.')
    if continuar == 'N':
        print('\033[34mANALISANDO...\033[m')
        sleep(1)
        print('\033[32mCRIANDO TABELA...\033[m')
        sleep(2)
        os.system('cls')
        break


print('='*40)
print('{:^40}'.format('ANALISE DE DADOS'))
print('='*40)
print(''' PESSOAS +18 |  HOMENS | MULHERES -20
        \033[34m{}    |    {}     |    {}\033[m
'''.format(maior_Idade, count_M, count_F_Idade))


print('FIM!')