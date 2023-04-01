# 37 - Escreva um programa que leia um número inteiro qualquer peça
# para o usuario escolher qual será a base de conversão:
#
# - 1 não binario
# - 2 para octal
# - 3 para hexadecimal

while True:  ## Utilizado pra repetir o programa.
    print('\033[7mCONVERSOR DE NÚMEROS\033[m')

    n = int(input('\033[4mDigite um número\033[m: '))
    print('- - - -' * 5)
    print('[\033[34m1\033[m] Hexadecimal \n'
          '[\033[34m2\033[m] Binario \n'
          '[\033[34m3\033[m] Octal \n'
          '[\033[31mx\033[m] Sair ')

    escolha = input('Escolha uma \033[4;34mopção\033[m: ').upper()

    if escolha == 'X':
        print('Até breve!')
        break
    elif escolha == '1':
       esc1 = hex(n)
       print(f'Em hexadecimal seu número é: {esc1[2:]}')
    elif escolha == '2':
        esc2 = bin(n)
        print(f'Em binario seu número é: {esc2[2:]}')
    elif escolha == '3':
        esc3 = oct(n)
        print(f'Em octal seu número é: {esc3[2:]}')
    else:
        print('Opção Invalida!')

    print('- - - -' * 5, '\n' )
