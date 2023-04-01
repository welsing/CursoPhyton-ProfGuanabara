# 53 - Crie um programa que leia uma frase qualquer e
# diga se ela é um palindromo, desconsiderando os espaços.
# ex: Após a Sopa
# A sacada da casa
# A torre da derrota
# O lobo ama o bolo
# Anotaram a data da maratona

frase = input('Diga uma frase: ').replace(' ', '').upper()
inverte = frase[::-1]
print(f'{frase} invertido fica {inverte}')

if frase == inverte:
    print('Legal, temos um palindromo. Podemos ler de trás para frente.')
else:
    print('AA, a frase não é um palindromo. ')



