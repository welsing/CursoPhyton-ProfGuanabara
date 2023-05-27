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
print(f'O menor peso cadastrado foi {menor} das pessoas: ', end='')
for v, p in enumerate(pessoas):
    if pessoas[v][1] == menor:
        print(f"[{pessoas[v][0]}]", end=' ')
print()
print(f'O maior peso cadastrado foi {maior}kg das pessoas: ', end='')
for v, p in enumerate(pessoas):
    if pessoas[v][1] == maior:
        print(f"[{pessoas[v][0]}]", end=' ')