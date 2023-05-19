# 088 - Faça um programa que ajude um jogador da MEGA-SENA a criar palpites. O programa vai perguntar
# quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo 
# cadastrando tudo em uma lista composta.

from random import sample
from time import sleep
jogos = []
print('#'*40)
print('{:^57}'.format('GERADOR \033[33mMEGA\033[m-\033[32mSENA\033[m'))
print('#'*40)

question = int(input('Quantos jogos quer \033[34msortear?\033[m: '))

print('{:-^38}'.format('\033[4mGerando DADOS\033[m'))
for i in range(0, question):
    sleep(2)
    sorteados = sample(range(1, 60), 6)
    print(f'JOGO {i+1}: {sorteados}')
    jogos.append(sorteados[:])
    sorteados.clear()
print('FIM!')
print('{:^40}'.format('>Obrigado Pela Preferencia!<'))
