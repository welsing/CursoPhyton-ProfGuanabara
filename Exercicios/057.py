# 057 - Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores "M" ou "F".
# Caso esteja errado, peça para digitar novamente até ter um valor correto


#                 MINHA SOLUÇÃO
# sexn = 1
# while sexn != 0:
#     sex = input('Qual seu sexo? F/M: ').strip().upper()[0]
#     if sex == 'F':
#         sexn = 0
#     if sex == 'M':
#         sexn = 0
#     if sexn != 0:
#         print('Escolha invalida! Digite novamente')
# print('Acabou')

#      VERSÃO DO GUANABARA

# strip para tirar os espaços, e o [0] para escolher só a primeira letra caso o usuario digite "MASCULINO"
sexo = input('Informe seu sexo [M/F]: ').strip().upper()[0]

while sexo not in 'FM':
    sexo = input(
        ' Dados \033[31mINVALIDOS\033[m! \n Informe seu sexo [M/F]: ').strip().upper()[0]
print(f'Pronto, sexo {sexo} escolhido.')
