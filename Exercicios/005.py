n = int(input('Me diga um numero: '))

print('Antes dele vem \033[1;031m{}\033[m o numero é \033[033m{}\033[m e depois dele vem \033[032m{}\033[m, correto?'.format(n - 1, n, n + 1))