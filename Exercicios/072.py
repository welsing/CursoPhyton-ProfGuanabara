
# 072 - Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso de ZERO até VINTE.
# seu programa devera ler um número pelo teclado e mostra-lo por extenso.

tupla = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez'
         , 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezeseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')
while True:
    while True:
        n = int(input('Digite um número (1 a 20): '))
        if 20 >= n >= 0:
            break
        else:
            print('Tente novamente!') 
    print(f'Você escolheu o número \033[34m{tupla[n]}\033[m')
    continuar = input('Quer continuar? [S/N]: ').upper()[0]
    if continuar == 'N':
        break
print('FIM!')
