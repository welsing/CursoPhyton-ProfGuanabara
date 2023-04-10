# 062 - Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
#  O programa encerra quando ele disser que quer mostrar 0 termos.
# termo = 1
# razao = 1

# while termo != 0:
#     print('\033[34mGERADOR DE PA\033[m | DIGITE \033[4;31m0\033[m PARA \033[31mSAIR\033[m')
#     termo = int(input('Digite o termo: '))
#     if termo != 0:
#         razao = int(input('Digite uma razão: '))
#         decimo = termo + 10 * razao
#         for pa in range(termo, decimo, razao):
#             print(f'{pa}', end=' > ')
#         print('ACABOU! \n')

# ENTENDI O ENUNCIADO ERRADO, ERA PRA MOSTRAR MAIS NÚMEROS, NÃO PRA PEDIR PRA REESCREVER OS TERMOS.
# CORRIGINDO: 

termo = int(input('Digite um termo: '))
razao = int(input('Digite uma razão: '))
count = 0
mostrar_Termo = 10
quantidade_Termos = 0
while mostrar_Termo != 0:
    while count != mostrar_Termo:
        print(f'{termo}', end=' > ')
        termo += razao
        count += 1
        quantidade_Termos += 1
    count = 0
    mostrar_Termo = int(input('PAUSA! \nQuantos termos que mostrar mais?: '))
print(f'Fim do programa, você viu {quantidade_Termos} termos!')
