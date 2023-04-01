# 49 - Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuario
# escolher, só que agora utilizando um laço for.

print('{:^30}'.format('\033[4mGERADOR DE TABUADA\033[m'))

n = int(input('DIGITE UM NÚMERO: '))

print(f'''\033[7m=== TABUADA DE {n} ===\033[m''')
for c in range(1, 11):
        print('{:^20}'.format('\033[34m{}\033[m x \033[34m{:2}\033[m = \033[32m{}\033[m'.format(n, c, n*c)))
