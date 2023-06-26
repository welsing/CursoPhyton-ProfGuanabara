# 099 - Faça um programa que tenha uma função chamada maior(), que receba varios parametros de valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

from random import randint as rd

def maior (*num):
    print(' -=-=- PROCURANDO O MAIOR NÚMERO -=-=-')
    for c, n in enumerate(num):
        if c == 0:
            maior = n
        elif n > maior:
            maior = n

    print(f"Os números que pediu para analisar foi : {num}")
    print(f'O maior número foi: {maior}')


##   TENTAR TERMINAR ISSO DEPOIS....
def menor(*num):
    print(' -=-=- PROCURANDO O MENOR NÚMERO -=-=-')
    for c, n in enumerate(num):
        if c == 0:
            menor = n
        elif n < menor:
            menor = n
    print(f"Os números que pediu para analisar foi : {num}")
    print(f'O menor número foi: {menor}')

maior(5,5,3,6,8,2,1,8,4,5,22,2,5,7,5,6)
menor(rd(0, 99),rd(0, 99),rd(0, 99),rd(0, 99),rd(0, 99),rd(0, 99),rd(0, 99),rd(0, 99),rd(0, 99),rd(0, 99),rd(0, 99))
maior(rd(0, 99),rd(0, 99),rd(0, 99))
maior(rd(0, 99),rd(0, 99),rd(0, 99),rd(0, 99),rd(0, 99),rd(0, 99),rd(0, 99),rd(0, 99))
maior(0)



# Só da certo se não colocar * no parametro
# def rand():
#     num = list()
#     for n in range(1, rd(5, 13)):
#         num.append(rd(0, 99))
    
#     for i in range(0, len(num)):
#         return(num[i])
    
# maior(rand())


