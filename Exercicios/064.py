# 064 - Crie um programa que leia vários números inteiros pelo teclado. 
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. 
# No final, mostre quantos números foram digitados e qual foi a soma entre eles(Desconsiderando o flag)

soma = 0
count = 0
n = int(input('Digite um número ou 999 para parar: '))
while n != 999:
    soma += n
    count += 1
    n = int(input('Digite um número ou 999 para parar: '))
print(f"Você digitou {count} números")
print(f'E a soma entre eles é {soma}')
