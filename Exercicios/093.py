# 093 - Crie um programa que gerencie o aproveitamento de um JOGADOR DE FUTEBOL. O programa vai
# ler o NOME DO JOGADOR e QUANTAS PARTIDAS ele jogou. depois vai ler a QUANTIDADE DE GOLS feitos em cada partida
# No final, tudo isso será guardado em um dicionario, incluindo o total de gols feitos durante o dicionario.
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

    # O ESPERADO -> jogador = [{'NOME':'Bernardo', 'PARTIDAS':5, 'totalGols':7}, {'jogo1':2,'jogo2':0,'jogo3':1,'jogo4':0,'jogo5':4}]


