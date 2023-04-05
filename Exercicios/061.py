# 061 - Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, 
# mostrando os 10 primeiros termos da progressão usando a estrutura while

termo = int(input('Insira um termo: '))
razao = int(input('Insira uma razão: '))
count = 0
print('{:^30}'.format(f'ESTÁ É A PA DE {razao}'))
while count != 10:
    if count < 9:
        print(f'{termo}', end=' > ')
    else:
        print(f'{termo}')
    termo += razao
    count += 1
print('FIM!')