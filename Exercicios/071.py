# 071 - Crie um programa que simule o funcionametno de um caixa eletronico. 
# No inicio, pergunte ao usuario qual será o valor sacado (número inteiro) 
# e o programa vai informar quantas cédulas de cada valor serão entregues. 
# obs: Considere que o caixa possui as cedulas de 50, 20, 10 e 1

from time import sleep
from os import system
cinquenta = vinte = dez = um = 0
system('cls')
print('#'*30)
print('{:^30}'.format('CAIXA ELETRONICO'))
print('#'*30)
caixa = int(input('SACAR R$: '))

while caixa >= 50:
    cinquenta += 1
    caixa -= 50
while caixa >= 20:
    vinte += 1
    caixa -= 20
while caixa >= 10:
    dez += 1
    caixa -= 10
while caixa >= 1:
    um += 1
    caixa -= 1

print('{:=^30}'.format(' IMPRIMINDO '))
print(f'{cinquenta} NOTAS DE 50')
sleep(1)
print(f'{vinte} NOTAS DE 20')
sleep(1)
print(f'{dez} NOTAS DE 10')
sleep(1)
print(f'{um} NOTAS DE 1')