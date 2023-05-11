# 083 - Crie um programa onde o usuario digite uma expressão qualquer que use parenteses. 
# Seu aplicativo deverá analisar se a expressão passada está com parenteses abertos e fechados na ordem correta.


exp = input('Digite uma expressão: ')

openCol = openParen = openChaves = 0

expressao = ''
if '[({})]' in exp:
    for i in range(len(exp)):
        if exp[i] == '[':
            openCol += 1
else:
    print('Expressão Válida')

    