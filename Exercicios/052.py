# 52 - Faça um programa que leia um número inteiro, e diga se ele é ou não um número primo.

n = int(input('ME FALE UM NÚMERO: '))
div = 0
for c in range(1, n+1):
    if n % c == 0:
        print('\033[033m', end=' ')
        div += 1
    else:
        print('\033[031m', end=' ')
    print('{}'.format(c), end=' ')
print('\n\033[mO número {} pode ser divisivel {} vezes'.format(n, div))

if div == 2:
    print('E por isso ele é PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')
