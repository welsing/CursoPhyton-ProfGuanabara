#29 - Escreva um programa que leia a velocidade de um carro se ele ultrapassar
# 80kh/h, mostre uma mensagem dizendo que ele foi multado
# A multa vai custar R$7,00 por cada km acima do limite

vel = float(input('Qual velocidade do carro?: '))
multa = (vel-80)*7

if vel > 80:
    print("\033[7;33mPOLICIA FEDERAL\033[m - Você ultrapassou o limite de velocidade e será \033[31mmultado\033[m!")
    print("Sua velocidade estava em \033[31;1m{:.0f}\033[mkm/h, e por isso será \033[4mmultado\033[m em R$\033[32m{:.2f}\033[m.".format(vel, multa))
    print("\033[42mDirija com segurança!\033[m")
else:
    print("Você segue as leis de transito. :) ")
