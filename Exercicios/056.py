# 56 - Desenvolva um programa que lia o NOME, IDADE e SEXO de 4 pessoas. No final do programa, mostre:
# -> A média de idade dos grupo.
# -> Qual o nome do homem mais velho.
# -> Quantas mulheres tem menos de 20 anos.

pessoas = []
novinhas = 0
maisvei = ''
maisveii = 0
somaidade = 0
for i in range(1, 5):
    print(F'---- {i} PESSOA ----')
    nome = input('Nome:  ').strip()
    idade = int(input('Idade: '))
    sexo = input('Sexo M/F: ').upper().strip()
    somaidade += idade
    if sexo == 'M':
        sexo = 'Homem'
    elif sexo == 'F':
        sexo = 'Mulher'
    pessoas.append({'Nome': nome, 'Idade': idade, 'Sexo': sexo})
    if sexo == 'Mulher' and idade < 20:
        novinhas += 1
    if sexo == 'Homem':
        maisvei = nome
        maisveii = idade
        if idade > maisveii:
            maisvei = nome
            maisveii = idade

print(f'A media das idades do grupo é {somaidade/4}')
print(f'Existem {novinhas} Mulheres com menos de 20 anos')
print(f'O homem mais velho tem {maisveii} anos e se chama {maisvei}')

for grupos in range(0, 4):
    print(f'PESSOA {grupos+1}')
    print(pessoas[grupos])