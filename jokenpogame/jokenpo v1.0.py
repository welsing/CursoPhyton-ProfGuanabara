import random
import time

print("\033[1;30m-=-" * 10)
print(" "*8, "\033[1;33mJO\033[1;34mKEN\033[1;35mPO\033[m \033[31mGAME\033[m")
print("\033[1;30m-=-\033[m" * 10)
pedra = 1
papel = 2
tesoura = 3
print("Selecione sua jogada. "
      "\n (1) - \033[4;36mPedra\033[m "
      "\n (2) - \033[4;36mPapel\033[m "
      "\n (3) - \033[4;36mTesoura\033[m")
jogador = (int(input("---------------: ")))
pc = random.choice([1, 2, 3])
print("\033[4mPEDRA, PAPEL E TESOUUUUURA!\033[m ")
time.sleep(2)
if jogador == 1 and pc == 2:
    print("Eu escolho \033[4;34mPAPEL\033[m!")
    print("HAHAHA! \033[1;31mPERDEU\033[m! :\033[31mP\033[m")

elif jogador == 1 and pc == 3:
    print("Eu escolho \033[4;34mTESOURA\033[m!")
    print("Af, voce \033[32;1mGANHOU\033[m, pode comer meu cuzin *-*")

elif jogador == 2 and pc == 1:
    print("Eu escolho \033[4;34mPEDRA\033[m!")
    print("Af, você \033[32;1mGANHOU\033[m, irei te mamar. :c")

elif jogador == 2 and pc == 3:
    print("Eu escolho \033[4;34mTESOURA\033[m!")
    print("HAHAHA! \033[1;31mPERDEU\033[m, CORNO.")

elif jogador == 3 and pc == 1:
    print("Eu escolho \033[4;34mPEDRA\033[m!")
    print("\033[1;31mPERDEU\033[m! TA ME DEVENDO UM \033[1;35mAÇAÍ\033[m!")

elif jogador == 3 and pc == 2:
    print("Eu escolho \033[4;34mPAPEL\033[m!")
    print("Você \033[32;1mGANHOU\033[m, bora denovo?")


elif jogador == 1 and pc == 1:
    print("Eu escolho \033[4;34mPEDRA\033[m!")
    print("AAA deu \033[4;33mEMPATE\033[m :P")

elif jogador == 2 and pc == 2:
    print("Eu escolho \033[4;33mPAPEL\033[m!")
    print("AAA deu \033[4;33mEMPATE\033[m :P")

elif jogador == 3 and pc == 3:
    print("Eu escolho \033[4;34mTESOURA\033[m!")
    print("AAA deu \033[4;33mEMPATE\033[m :P")

else:
    print("Tem que escolher 1, 2 ou 3 né!!!")
