# 39 - Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
#
# - Se ele ainda vai se alistar ao serviço    # Use o datetime
# - Se é a hora de se alistar.
# - Se já passou do tempo do alistamento
# Seu programa programa também deverá mostrar o tempo que falta ou que passou do prazo.

import datetime

print('\033[46;32;1mJUNTA MILITAR BRASILEIRA\033[m')

name = str(input('Qual seu nome?: '))
nasc = int(input('Qual seu ano de nascimento?: '))
ano = datetime.datetime.today().year
idade = ano - nasc

print('É um prazer te conhecer \033[4;33m{}\033[m!'.format(name))
print('Quem nasceu em \033[34m{}\033[m tem \033[34m{}\033[m anos em \033[34m{}\033[m.'.format(nasc, idade, ano))
if ano-nasc == 18:
    print('Tenho de lhe informar que você deve se \033[4malistar\033[m ao \033[32;1mexercito\033[m esse ano.')
elif ano-nasc > 18:
    print('Oh, no! Você passou do prazo de se \033[4malistar\033[m! \n\033[31mCorra\033[m até a \033[42:1mjunta militar\033[m mais proxima!')
    print('Já se passaram \033[31m{}\033[m anos da data de seu \033[4;32malistamento\033[m!'.format(ano-(nasc+18)))
    print('Seu ano de alistamento foi em \033[31m{}\033[m'.format(nasc+18))
else:
    print('Calma, jovem gafanhoto. Logo chegará sua hora de capinar \033[32mgrama\033[m!')
    print('Você deverá se alistar em \033[31m{}\033[m anos. Fique ligado!'. format((nasc+18)-ano))
    print('Seu ano de alistamento será em \033[34m{}\033[m'.format(nasc+18))




