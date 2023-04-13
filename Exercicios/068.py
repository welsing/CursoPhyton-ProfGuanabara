# 068 - Faça um programa que o usuario jogue PAR ou IMPAR com o computador. O jogo só será interrompido quando o jogador PERDER
# Mostrando o total de vitorias consecutivas do jogador.

from random import randint
from time import sleep
import os
import sys



count = 0
while True:
    while True:
        os.system('cls') or None
        print('=-'*15)
        print('{:^35}'.format('IMPAR OU PAR \033[34mGAME\033[m'))
        print('=-'*15)
        user_Choice = input('\033[4mIMPAR\033[m ou \033[4mPAR\033[m? [I/P]: ').strip().upper()[0]
        if user_Choice == 'I':
            user_Choice = 'IMPAR'
            pc_Choice = 'PAR'
            break
        elif user_Choice == 'P':
            user_Choice = 'PAR'
            pc_Choice = 'IMPAR'
            break
        else:
            print('Ops, escolha \033[31mINVALIDA!\033[m Tente novamente.')
            sleep(3)
            os.system('cls') or None
    
    user_Number = int(input('Digite um \033[34mnúmero\033[m: '))
    
    pc_Number = randint(0,100)
    soma = user_Number + pc_Number

    if soma%2 != 0:
        print('')
        win = 'IMPAR'
    elif soma%2 == 0:
        win = 'PAR'

    print('#'*30)
    print('IMPAR')
    sleep(0.5)
    print('     OU')
    sleep(0.5)
    print('         PAR!')
    sleep(0.5)                                            
    print(f'😼 JOGADOR: \033[34m{user_Choice}\033[m | \033[34m{user_Number}\033[m')
    print(f'🖥️  COMPUTADOR:\033[36m{pc_Choice}\033[m | \033[36m{pc_Number}\033[m')
    print(f'O total foi \033[33m{user_Number+pc_Number}\033[m que é \033[33m{win}\033[m')
    print('#'*30)
    if user_Choice == win:
        count += 1
        print('PARABENS! Você \033[32mGANHOU!\033[m')
        print(f'\033[7mVITORIAS CONSECUTIVAS: \033[32m{count}\033[m')
        while True:
            proxima = input('\033[4mQUER CONTINUAR?\033[m [S/N]:').upper()[0]
            if proxima == 'N':
                print('Até a proxima...')
                sys.exit()
            elif proxima == 'S':
                break
    else:
        print('Você \033[31mPERDEU!\033[m')
        break
print('Até a proxima...')


        
