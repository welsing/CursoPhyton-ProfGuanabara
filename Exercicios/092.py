# 092 - Crie um programa que leia NOME, ANO de NASC. e CARTEIRA DE TRABALHO e cadastre-os (com idade)
# em um DICIONARIO. se por acaso a CTPS for diferente de 0, o dicionario receberá também o ano da contratação
# e o salario. Calcule e acrescente, alem da idade, com quantos anos a pessoa vai se aposentar.

from datetime import date
pessoa = {}

pessoa['nome'] = input('Nome: ')
pessoa['idade'] = date.today().year - int(input('Ano de Nascimento: '))
pessoa['CTPS'] = input('Carteira de Trabalho (0 não tem): ')

if pessoa['CTPS'] != '0':
    pessoa['Ano de Contratação'] = int(input('Ano de contratação: '))
    pessoa['Salario'] = float(input('Salario: '))
    pessoa['Aposentadoria'] = (pessoa['Ano de Contratação'] - (date.today().year - pessoa['idade'])) + 35


for k, v in pessoa.items():
    print(f'{k.title()} tem o valor {v}')