# 057 - Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores "M" ou "F". 
# Caso esteja errado, peça para digitar novamente até ter um valor correto

sexn = 1
while sexn != 0:
    sex = input('Qual seu sexo? F/M: ').strip().upper()
    if sex == 'F':
        sexn = 0
    if sex == 'M':
        sexn = 0
    if sexn != 0:
        print('Escolha invalida! Digite novamente')

print('Acabou')