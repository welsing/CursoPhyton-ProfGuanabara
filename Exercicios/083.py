# 083 - Crie um programa onde o usuario digite uma expressão qualquer que use parenteses. 
# Seu aplicativo deverá analisar se a expressão passada está com parenteses abertos e fechados na ordem correta.


exp = input('Digite uma expressão: ')
verificador = []

for i in exp:
    if i == '(':
        verificador.append('(')
    elif i == ')':
        if len(verificador) > 0:
            verificador.pop()
        else:
            verificador.append(')')
            break

if len(verificador) > 0:
    print("Sua expressão está errada!")
else:
    print("Sua expressão está correta!")



    