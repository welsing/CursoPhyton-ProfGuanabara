# 50 - Desenvolva um programa que leia seis números inteiros,
# e mostre a soma apenas daqueles que forem pares. Se o valor digitado for Impar desconsidere-o
s = 0
count = 0
for c in range(0,6):
    n = int(input('Digite um número'))
    if n % 2 == 0:
        s = s + n
        count += 1
print('A soma dos {} números pares dos valores digitados é {}'.format(count, s))