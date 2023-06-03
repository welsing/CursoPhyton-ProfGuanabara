# 091 - Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatorios. 
# guarde esses resultados em um dicionario. No final, coloque esse dicionario em ordem, sabendo que
# o vencedor tirou o maior numero no dado.

import operator
from random import randint
from time import sleep

jogo = {'Jogador 1':randint(1,6),
        'Jogador 2':randint(1,6),
        'Jogador 3':randint(1,6),
        'Jogador 4':randint(1,6)}

print('---- JOGANDO DADOS ----')
for j, d in jogo.items():
    print(f"O {j} jogou o dado e caiu {d}!")
    sleep(1)
jogoEmOrdem = sorted(jogo.items(), key=operator.itemgetter(1), reverse=True)
print('== CLASSIFICAÇÃO DA PARTIDA ==')
for i, j in enumerate(jogoEmOrdem):
    print(f"  {i+1}º Lugar: {j[0]} com {j[1]} pontos.")
    sleep(0.5)
