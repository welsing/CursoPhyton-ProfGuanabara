# 098 - FAça um programa que tenha uma função chamada contador(), que receba tres parametros:
# Inicio, fim e passo e realize a contagem. Seu programa tem que realizar 3 contagens atraves da função criada.
# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) Uma contagem personalizada

from time import sleep

def sep():
    print("=-"*20)


def contador(ini, fim, passo):
    sep()
    if passo == 0:
        passo = 1
    elif passo < 0:
        passo = abs(passo)
    print(f'Contagem de {ini} até {fim} de {passo} em {passo}')
    sleep(1)
    if ini < fim:
        for count in range(ini, fim+1, passo):
            print(count, end=' ')
    elif fim < ini:
        for count in range(ini, fim-1, -passo):
            print(count, end=' ')
    
    print(' -> FIM!')


# Programa Principal
contador(1, 10, 1)
sleep(2)
contador(10, 0, 2)
sleep(2)
sep()
print('Agora é a SUA vez de personalizar a contagem!')
contador(int(input('Incio: ')), int(input('Fim: ')), int(input('Passo: ')))


