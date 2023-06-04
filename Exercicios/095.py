# 095 - Aprimore o desafio 93 para que ele funcione com varios jogadores. incluindo um sistema de visualização
# de detalhes de aproveitamento de cada jogador.

from time import sleep
jogador = [{}, {}]

print('---> CADASTRO JOGADOR TEMPORADA DE VERÃO <---')
jogador[0]['NOME'] = input('Nome do jogador: ').title()
jogador[0]['PARTIDAS'] = int(input('Partidas Jogadas: '))
jogador[1]['TotalGols'] = 0
print('=- GOLS POR PARTIDA -=')
for i in range(1, jogador[0]['PARTIDAS']+1):
    jogador[1][f'Jogo {i}'] = int(input(f'Jogo {i} | GOLS: '))
    jogador[1]['TotalGols'] += jogador[1][f'Jogo {i}'] 

print(f'-= DADOS DO JOGADOR {jogador[0]["NOME"]} =-')

for k, v in jogador[0].items():
    print(f'Em {k} foi registrado {v}')
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=')
for k, v in jogador[1].items():
    sleep(1)
    print(f'Em {k} foi registrado {v} gols!')