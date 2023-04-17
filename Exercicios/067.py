# 067 - Faça um programa que mostre a tabuada de varios números, um de cada vez, para cada valor digitado ao usuario. 
# O programa será interrompido quando o número solicitado for negativo.
from time import sleep
print('#'*30)
print('{:^30}'.format('Gerador de Tabuadas'))
print('#'*30)
n = 0
while True:
   
    n = int(input('Digite um \033[33mnúmero\033[m: '))
    if n <= 0:
        print('FECHANDO PROGRAMA...')
        sleep(3)
        break 
    print('~'*30)
    print('{:^30}'.format(f'Tabuada de {n}'))
    for x in range(1, 11):
        print(f'          {n} x {x} = {x*n}')
    print('#'*30)
    print('\033[7mVAMOS CONSULTAR OUTRA TABUADA?\033[m (\033[31m0\033[m) para sair')
print('❌')