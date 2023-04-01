# 55 - Faça o programa que leia o PESO de cinco pessoas.
# No final, mostre qual foi o maior e o menor peso lidos

pesos = []
for c in range(1,6):
    peso = float(input(f'Digite o {c} peso (Kg): '))
    pesos.append(peso)
pesosordem = sorted(pesos)
maiorpeso = pesosordem[-1]
menorpeso = pesosordem[0]

print(f'O maior peso foi {maiorpeso}Kg e o menor foi {menorpeso}Kg')