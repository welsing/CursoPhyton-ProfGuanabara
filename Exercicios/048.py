# 48 - Faça um programa que calcule a soma entre todos os números
# ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500

somar = 0
count = 0
for c in range(1,501, 2):
    if c % 3 == 0:
        print(c, end=' ')
        somar += c
        count += +1
print(f'\nA soma de todos os números {count} impares multiplo de 3 de 1 a 500 é: {somar}')
