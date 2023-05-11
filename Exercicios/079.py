# 079 - Crie um programa onde o usuario possa digitar, varios valore númericos, e cadastre em uma lista.
# Caso o número já exista la dentro, ele não será adicionado.
# No final, será exibido todos os valores únicos em ordem CRESCENTE. 

lista = []
while True:
    n = int(input('Digite um valor: '))
    if n not in lista:
        print(f'Valor {n} \033[32madicionado\033[m')
        lista.append(n)
    else:
        print('Esse \033[31mvalor\033[m já está na lista.')
    while True:
        sorn = input('Quer continuar? [S/N]: ').upper().strip()[0]
        if sorn in 'SN':
            break
        else:
            print('Escolha \033[31mINVALIDA\033[m! Tente novamente.')
    if sorn == 'N':
        break
    print('='*25)
lista.sort()
print(f'Lista na ordem crescente: {lista}')
        

