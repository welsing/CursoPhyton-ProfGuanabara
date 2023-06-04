# 095 - Aprimore o desafio 93 para que ele funcione com varios jogadores. incluindo um sistema de visualização
# de detalhes de aproveitamento de cada jogador.

from os import system
from time import sleep
jogador = dict()
jogadores = list()
partidas = list()


print('---> CADASTRO JOGADOR TEMPORADA DE INVERNO <---')
while True:
    partidas.clear()
    jogador['NOME'] = input('\033[34mNome\033[m do Jogador: ').title().strip()
    while True:
        try: 
            jogador['PARTIDAS'] = int(input(f'Quantas partidas \033[34m{jogador["NOME"]}\033[m jogou?: '))
            break
        except (ValueError):
            print('\033[31mERROR!\033[m Digite apenas números. Tente novamente!')
    for i in range(1, jogador['PARTIDAS']+1):
        while True:
            try: 
                partidas.append(int(input(f'   Quantos \033[34mgols\033[m na partida {i}?: ')))
                break
            except (ValueError):
                print('\033[31mERROR!\033[m Digite apenas números. Tente novamente!')
    jogador['GOLS'] = partidas[:]
    jogador['totalGols'] = sum(partidas)
    jogadores.append(jogador.copy())
    while True:
        sorn = input('Quer continuar? [S/N]: ').strip()[0]
        if sorn in 'SNsn':
            break
        print('\033[31mERROR!\033[m Responda apenas [S]im ou [N]ão! Tente novamente.')
    if sorn in 'Nn':
        print('-='*25)
        break
    print('-'*40)

system('cls')
print(f'{"Cod.":<5}\033[34m{"Jogador":<15}\033[m{"Gols":<20}{"Total"}')
for i in range(0, len(jogadores)):
    print(f"{i+1:<5}{jogadores[i]['NOME']:<15}{jogadores[i]['GOLS']}{jogadores[i]['totalGols']:}")
print('-='*25)

while True:
    while True:
        while True:
            try:
                n = int(input('Quer os dados de qual jogador? [999] p/ \033[31mSair\033[m: '))
                break
            except ValueError:
                print('\033[31mERROR!\033[m Digite apenas numeros. tente novamente!')
                print('-'*20)
        if n in range(1, len(jogadores)+1) or n == 999:
            break
        print('\033[31mERROR!\033[m Jogador não existe, tente novamente!')
        print('-'*20)
    
    if n == 999:
        print('>> ATÉ LOGO. <<')
        break
    n = n - 1
    print(f">>\033[34m{jogadores[n]['NOME']}\033[m jogou \033[33m{jogadores[n]['PARTIDAS']}\033[m partidas.")
    for i, v in enumerate(jogadores[n]['GOLS']):
        print(f'  - Na \033[4m{i+1}º partida\033[m fez \033[32m{v}\033[m gols.')
    print('-'*50)
