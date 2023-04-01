# 28 - faça o computador "pensar" num numero de 0a5 e pça para o
# usuario descobrir qual numero foi escolhido e dizer se venceu

from random import randint
from time import sleep
print("-=-" * 20)
print("Vou pensar num numero de \033[40m1 a 5\033[m. Tente adivinha...")
print("-=-" * 20)
pc = randint(1, 5)
user = int(input("Qual \033[4mnumero\033[m vc acha q pensei? : "))
print("\033[33;4mPROCESSANDO...\033[m")
sleep(2)
if user == pc:
    print("Muito bem, voce \033[32macertou\033[m")
else:
    print("Pois bem, vc não le mentes né! \033[31mERROU\033[m!")
print("-- O numero que pensei foi \033[34m{}\033[m".format(pc))
