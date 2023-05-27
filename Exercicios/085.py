# 085 - Crie um programa onde o usuário possa digitar sete valores númericos e cadastreo-os em uma lista única
# que matenha separado os valores pares e impares. No final, mostre os valores pares e impares em ordem crescente.

lista = [[], []]
for i in range(0, 7):
    n = int(input(f'Digite o {i+1} valor número: '))
    if n % 2 == 0:
        lista[0].append(n)
    else:
        lista[1].append(n)
lista[0].sort()
lista[1].sort()

print(f'Valores par: {lista[0]}')
print(f'Valores impares: {lista[1]}')

