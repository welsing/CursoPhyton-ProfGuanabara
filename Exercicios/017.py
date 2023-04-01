'''from math import sqrt
cop = float(input('Qual cateto oposto? : '))
cadj = float(input('Qual cateto adjacente? :'))

h = (cop**2) + (cadj**2)

print('A hipotenusa dos catetos {} e {} é {:.2f}'.format(cop, cadj, sqrt(h)))'''

from math import hypot

co = float(input('Me informe o cateto oposto: '))
ca = float(input('Me informe o cateto adjacente: '))
h = hypot(co, ca)
print('A hipotenusa de {} e {} é igual a {}.'.format(co, ca, h))