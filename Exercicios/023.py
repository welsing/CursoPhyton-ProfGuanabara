num = int(input("Digite um numero de 0 a 9999: "))



u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

if num < 10000:
    print('Analisando o numero {}'.format(num))
    print('Milhar: {}'.format(m))
    print('Centena: {}'.format(c))
    print('Dezena: {}'.format(d))
    print('Unidade: {}'.format(u))
else: 
    print('Numero mt grande porra')
    