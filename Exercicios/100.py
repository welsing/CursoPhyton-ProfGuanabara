# 100 - Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somarPar()
# A primeira função vai sortear 5 números e vai coloca-los dentro da lista e a segunda função vai mostrar
# a soma entre todos os valores pares sorteados pela função anterior.
from random import randint as rd
from time import sleep

def sorteia(addList):
    print("Sorteando 5 valores para lista: ")
    for i in range(0,5):
        addList.append(rd(1,30))
        print(addList[i])
        sleep(0.5)
    print("PRONTO!")

def somaPar(addList):
    somaP = 0
    for i in addList:
        if i % 2 == 0:
            somaP += i

    print(f'Somando os valores pares de {addList}. Temos {somaP}')
    




numeros = list()

sorteia(numeros)
somaPar(numeros)

