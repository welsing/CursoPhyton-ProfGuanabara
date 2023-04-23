# 075 - Desenvolva um programa que leia 4 valores pelo teclado e guarde numa tupla. No final mostre:
# (a) Quantas vezes apareceu o valor 9
# (b) Em que posição foi digitado o primeiro 3
# (c) Quais foram os pares

valor1 = int(input('Digite um valor: '))
valor2 = int(input('Digite um valor: '))
valor3 = int(input('Digite um valor: '))
valor4 = int(input('Digite um valor: '))
tupla = valor1, valor2, valor3, valor4
print(f'Você digitou os valores: {tupla}')
vezes9 = tupla.count(9)
if vezes9 > 0:
    print(f'Você digitou {tupla.count(9)} vezes o número 9.')
else:
    print('O número 9 não apareceu nenhuma vez.')

try: 
    primeiro3 = tupla.index(3)
    print(f'O primeiro tres é o {tupla.index(3)+1}º valor')
except ValueError:
    print('O 3 não se encontra em nenhuma posição.')

condição = 0
print('Os números pares são: ', end='')
for n in tupla:
    if n %2 ==0:
        print(n, end=' ')
        condição += 1

        
# for i in range(0,4):
#     par = tupla[i]
#     if par%2 == 0:
#         print(par, end=' ')
#           condição += 1
if condição == 0:
    print('\033[31mNão existem\033[m números pares')