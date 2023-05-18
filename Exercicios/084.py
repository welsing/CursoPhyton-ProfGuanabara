# 084 - Faça um programa que leia Nome e Peso de varias pessoas, guardando tudo em uma lista.
# No final, mostre:
# a) Quantas pessoas foram cadastradas
# b) Uma listagem com as pessoas mais pesadas
# c) Uma listagem com as pessoas mais leves

pessoas = []
dados = list()

while True:
    print('#'*30)
    nome = input('Nome: ')
    dados.append(nome)
    peso = float(input('Peso (KG):'))
    dados.append(peso)
    if len(pessoas) == 0:
        maior = menor = peso
    else:
        if maior < peso:
            maior = peso
        if menor > peso:
            menor = peso
    pessoas.append(dados[:])
    dados.clear()

    sorn = input("Deseja continuar? [S/N]: ").lower().strip()[0]
    if sorn == 'n':
        print('=-'*15)
        break

print(f'CADASTROS REALIZADOS: {len(pessoas)}')
print('Menores pesos cadastrados: ', end='')
for v, p in enumerate(pessoas):
    if pessoas[v][1] == menor:
        print(pessoas[v], end=' ')
print()
print('Maiores pesos cadastrados: ', end='')
for v, p in enumerate(pessoas):
    if pessoas[v][1] == maior:
        print(pessoas[v], end=' ')