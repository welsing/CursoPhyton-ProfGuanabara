import random
import time
# CABEÇALHO
print("\033[1;30m-=-" * 8)
print('{:^55}'.format(' \033[1;33mJO\033[1;34mKEN\033[1;35mPO\033[m \033[31mGAME\033[m '))
print("\033[1;30m-=-" * 8)

# VARIÁVEIS DO PLACAR
playercount = 0
pccount = 0

# Repetição
while True:
    print('{:^31}'.format("\033[7;4mPLACAR\033[m"))
    print('{:x^30}'.format('🤠 VOCÊ \033[32m{}\033[m x \033[31m{}\033[m PC 🤖 '.format(playercount, pccount)))
    print('- \033[34mSELECIONE SUA JOGADA\033[m -')
    print('''
    [\033[34m1\033[m] 🪨 Pedra 
    [\033[34m2\033[m] 🧻 Papel
    [\033[34m3\033[m] ✂️ Tesoura
    [\033[31mx\033[m] ❌ SAIR
    ''')
    # Computador seleciona a jogada
    pc = random.randint(1,3)
    # jogador seleciona a jogada
    player = input('\033[7mDigite sua jogada:\033[m ')


    # SAIR DO GAME
    if player == 'x':
        print("- Foi \033[37mdivertido\033[m jogar com \033[32mvocê\033[m! \033[4mAté logo\033[m!😘 ")
        break

    # PAUSA DE TENSÃO
    print('JO')
    time.sleep(0.5)
    print('  KEN')
    time.sleep(0.5)
    print('     PO!!!')
    time.sleep(0.5)

    player = int(player)
    print('=-' * 20)
    # CONDIÇÕES DE VITORIA
    if pc == 1 and player == 2:
        print('Eu escolho \033[34mPEDRA\033[m!🪨 \n Ah não! Você \033[32mGANHOU\033[m!')
        playercount = playercount + 1
    elif pc == 2 and player == 3:
        print('Eu escolho \033[34mPAPEL\033[m!🧻 \n Okay, \033[32mGANHOU\033[m! ponto pra você.')
        playercount = playercount + 1
    elif pc == 3 and player == 1:
        print('Eu escolho \033[34mTESOURA\033[m!✂️ \n AAAH *-* \033[32mGANHOU\033[m.')
        playercount = playercount + 1

    # CONDIÇÕES DE PERDA
    elif player == 1 and pc == 2:
        print('Eu escolho \033[34mPAPEL\033[m!🧻 \n hahaha! \033[31mPERDEU\033[m! \033[4mPONTO PARA MIM!\033[m')
        pccount = pccount + 1
    elif player == 2 and pc == 3:
        print('Eu escolho \033[34mTESOURA\033[m!✂️ \n TOMA ESSA! \033[31mPERDEU\033[m!')
        pccount = pccount + 1
    elif player == 3 and pc == 1:
        print('Eu escolho \033[34mPEDRA\033[m!🪨 \n Graza a deus pai. \033[31mPERDEU\033[m!  ')
        pccount = pccount + 1

    # CONDIÇÕES DE EMPATE
    elif player == 1 and pc == 1:
        print('Eu escolho \033[34mPEDRA\033[m!🪨 '
              '\n Ahh deu \033[33mEMPATE\033[m.')
    elif player == 2 and pc == 2:
        print('Eu escolho \033[34mPAPEL\033[m!🧻 '
              '\n \033[33mEMPATE\033[m! Ponto pra ninguêm.')
    elif player == 3 and pc == 3:
        print('Eu escolho \033[34mTESOURA\033[m!✂️ '
              '\n Avisa pro juiz não mexer no placar, \033[33mEMPATE\033[m!')

    # Caso o jogador não selecione certo.
    else:
        print('\033[31;7mOPÇÃO INVALIDA, TENTE NOVAMENTE\033[m')

    print('=-' * 20)

    print('\033[34mCARREGANDO PROXIMA PARTIDA...\033[m\n')
    time.sleep(3)

