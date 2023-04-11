# 068 - Faça um programa que o usuario jogue PAR ou IMPAR com o computador. O jogo só será interrompido quando o jogador PERDER
# Mostrando o total de vitorias consecutivas do jogador.

from random import randint
from time import sleep
import os



count = 0
while True:
    while True:
        print('=-'*15)
        print('{:^35}'.format('IMPAR OU PAR \033[34mGAME\033[m'))
        print('=-'*15)
        user_Choice = input('IMPAR ou PAR? [I/P]: ').strip().upper()[0]
        if user_Choice == 'I':
            user_Choice = 'IMPAR'
            pc_Choice = 'PAR'
            break
        elif user_Choice == 'P':
            user_Choice = 'PAR'
            pc_Choice = 'IMPAR'
            break
        else:
            print('Ops, escolha INVALIDA! Tente novamente.')
            sleep(3)
            os.system('cls') or None
    
    user_Number = int(input('Digite um número: '))
    

    print('IMPAR')
    sleep(0.5)
    print('     OU')
    sleep(0.5)
    print('         PAR!')
    sleep(0.5)

    pc_Number = randint(0,999)
    soma = user_Number + pc_Number

    print('#'*30)
    print(f'Você escolheu {user_Choice} e jogou {user_Number}')
    print(f'O computador escolheu {pc_Choice} e jogou {pc_Number}')
    print('#'*30)
    
    if soma%2 != 0:
        print('')
        win = 'IMPAR'
    elif soma%2 == 0:
        win = 'PAR'
    

    if user_Choice == win:
        count += 1
        print('PARABENS! Você GANHOU!')
        print(f'VITORIAS CONSECUTIVAS: {count}')
    else:
        break

print('Você PERDEU! Até a proxima...')
        
