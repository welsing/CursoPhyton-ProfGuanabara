# 41 - A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento
# de um atleta e mostre sua categoria
# - até 9 anos: Mirim
# - até 14 anos: Infantil
# - até 19 anos: Junior
# - até 20 anos: Senior
# - Acima: Master

import datetime

print('\033[44;4mCONFEDERAÇÃO NACIONAL DE NATAÇÃO\033[m')
print('Vamos descobrir qual sua categoria.')
print('''
 - até 9 anos: Mirim
 - até 14 anos: Infantil
 - até 19 anos: Junior
 - até 25 anos: Senior
 - Acima: Master
''')

name = input('Nome: ')
nasc = int(input('Ano de nasc: '))
ano = datetime.datetime.today().year
idade = ano-nasc
if idade <= 9:
    cat = 'Mirim'
# elif idade > 9 and idade <= 14:
# Não preicsava falar que idade é maior que 9, pois se ele passou do primeiro if, obvio que é maior que 9
elif idade <= 14: # correção
    cat = 'Infantil'
elif  idade <= 19:
    cat = 'Junior'
elif idade <= 25:
    cat = 'Senior'
else:
    cat = 'Master'

print('FICHA DO ATLETA \n NOME: {} \n IDADE: {} \n CATEGORIA: {}'.format(name, idade, cat))




