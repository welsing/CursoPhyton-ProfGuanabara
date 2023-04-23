# 073 - Crie uma tupla preenchida com os 20 primeiros colocados da tabela do Brasileirão, na ordem de colocação. 
# Depois mostre: 
# (a) Apenas os 5 primeiros colocados.
# (b) Os ultimos 4 colocados
# (c) Uma lista com os times em ordem alfabetica
# (d) Em que posiçãço na tabela está o time da Chapecoense.
from os import system

system('cls')
brasileirão = ('Flamengo', 'Fluminense', 'Paranaense', 'Botafogo', 'Vasco', 'Bragantino'
               , 'Corinthians', 'Palmeiras', 'Gremio', 'Fortaleza'
               , 'Internacional', 'Atletico M.', 'Cruzeiro', 'Chapecoense', 'Bahia'
               , 'SãoPaulo FC', 'Santos' , 'Goiás', 'América', 'Coritiba')

print('#' * 30)
print('{:^30}'.format('BRASILEIRÃO 2023'))
print('#' * 30)

print(f'Primeiros \033[32m5º Colocados\033[m: ', end='')
for i in range(0, 5):
    if i == 4:
        print(f'{i+1}º {brasileirão[i]}.')
    else: 
        print(f'{i+1}º {brasileirão[i]}', end=' - ')
print(' = ' * 30 )
print(f'Os ultimos \033[31m4 colocados\033[m foram: ', end='')
for i in range (1, 5):
    print(brasileirão[-i], end=' - ')
print('')
print(' = ' * 30 )
brasileirãoAlfabetic = sorted(brasileirão)
print('Todos os times em \033[34mordem alfabetica\033[m: ', end='')
for i in range(0, len(brasileirão)):
    if i != len(brasileirão)-1:
        print(f'{brasileirãoAlfabetic[i]}', end=', ')
    else:
        print(f'{brasileirãoAlfabetic[i]}.')
print(' = ' * 30 )
posicao = brasileirão.index('Chapecoense')
print(f'O \033[32mChapecoense\033[m FC está em {posicao+1}º')

