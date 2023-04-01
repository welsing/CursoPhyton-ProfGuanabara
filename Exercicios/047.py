# 47 - Crie um programa que mostre na tela todos os números PARES entre 1 e 50
import time
for c in range(1, 51):
    if c % 2 == 0:
        print(c, end=' ')
        time.sleep(0.2)
print('ACABOU')
