# 46 - Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artificio,
# indo de 10 até 0, com uma pausa de 1 segundo entre eles
from time import sleep

for fogos in range(10, 0, -1):
    print('🗣️ {} '.format(fogos))
    sleep(1)
print('{:^40}'.format('🎆🎆🎆🥳🥳 FELIZ ANO NOVOOO !! 🎉🎉🎆🎆'))