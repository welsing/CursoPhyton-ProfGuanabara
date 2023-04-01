n = int(input('Me diga um \033[46;1mnumero\033[m: '))
d = n * 2 # dobro
t = n * 3 # triplo
# v = n ** (1/2) # Raiz quadrada 
v = pow(n, (1/2))

print('O \033[46;1mnumero\033[m é \033[4;35m{}\033[m \n seu dobro é \033[35m{}\033[m '
      '\n seu triplo é \033[35m{}\033[m '
      '\n e sua raiz é \033[31;40m{:.2f}\033[m'.format(n, d, t, v))
