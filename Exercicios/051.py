# 51 - Desenvolva um programa que leia o primeiro termo e a razão de uma PA(Progressão Aritmetica).
# No final, mostre os 10 primeiros termos dessa progressão.

print('GERADOR DE PROGRESSÕES ARITMETICAS')
termo = int(input('Insira o termo: '))
razao = int(input('Insira a razão: '))
decimo = termo + (11 - 1) * razao
print('ESTÁ É A PA DE {}'.format(razao))
for pa in range(termo, decimo, razao):
    print(pa, end=' > ')
print('ACABOU')



