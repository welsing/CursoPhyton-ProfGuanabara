# 099 - Faça um programa que tenha uma função chamada maior(), que receba varios parametros de valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

from random import randint

def maior (*num):
    print(' -=-=- PROCURANDO O MAIOR NÚMERO -=-=-')
    for c, n in enumerate(num):
        if c == 0:
            maior = n
        elif n > maior:
            maior = n

    print(f"Os números que pediu para analisar foi? : {num}")
    print(f'O maior número foi: {maior}')


##   TENTAR TERMINAR ISSO DEPOIS....
def menor(*num):
    print(' -=-=- PROCURANDO O MENOR NÚMERO -=-=-')
    for c, n in enumerate(num):
        if c == 0:
            menor = n
        elif n < menor:
            menor = n
    print(f"Os números que pediu para analisar foi? : {num}")
    print(f'O maior número foi: {menor}')

def rand():
    num = list()
    for n in range(1, randint(5, 13)):
        num.append(randint(0, 99))
    num = tuple(num)
    return(num)



maior(5,5,3,6,8,2,1,8,4,5,22,2,5,7,5,6)
menor(randint(0, 99),randint(0, 99),randint(0, 99),randint(0, 99),randint(0, 99),randint(0, 99),randint(0, 99))
maior(randint(0, 99),randint(0, 99),randint(0, 99),randint(0, 99),randint(0, 99),randint(0, 99),randint(0, 99),randint(0, 99),randint(0, 99),randint(0, 99),randint(0, 99))
menor(randint(0, 99),randint(0, 99),randint(0, 99))
maior(randint(0, 99),randint(0, 99),randint(0, 99),randint(0, 99),randint(0, 99),randint(0, 99),randint(0, 99),randint(0, 99))







