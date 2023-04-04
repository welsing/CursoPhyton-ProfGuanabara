# 060 - Faça um programa que leia um número qualquer e mostre o seu fatorial
# ex: 5 != 5x4x3x2x1 = 120 (Da pra fazer com while e for)


result = 1
n = ''
n = int(input('Digite um número: '))
for p in range(n, 0, -1):
    if p != 1:
        print(f'{p}x', end='')
    else:
        print(f'{p}', end='')
for i in range(1, n+1):
    result *= i
print(f' = {result}')




