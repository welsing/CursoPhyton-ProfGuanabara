# 058 - Melhore o jogo DESAFIO 028 onde o computador vai "PENSAR" em um número entre 0 e 10. 
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites 
# foram necessários para vencer.
#                           ESTÁ É MINHA VERSÃO DA RESOLUÇÃO DO EXERCICIO, TENTEI DEIXAR MAIS DIVERTIDO DO QUE A RESOLUÇÃO NO CURSO.
from random import randint
from time import sleep
import sys
import os
pc = randint(1, 10)

print(''' ---- \033[34m 🧠⁉️ JOGO DO ADIVINHA ⁉️🧠\033[m ----
Regras: 
- O robo irá \033[33mpensar\033[m em um número de 1 a 10;
- Você deverá tentar \033[32macertar\033[m o número que ele pensou;
- Caso acerte, você \033[7mganhará o jogo.\033[m;

Dicas:
- 😼 Se a palavra "PALPITES" estiver \033[36;4mcolorida\033[m, 
segnifica que você pode estar mais perto ou mais longe do número pensado.
                ------ \033[32mDICI\033[31mONAR\033[33mIO \033[33mDE \033[33mCO\033[31mRES\033[m ------
                \033[31mVERMELHO\033[m - LONGE DO NÚMERO PENSADO 😭
                \033[33mAMARELO\033[m - ESTÁ NO CAMINHO 🥳
                \033[32mVERDE\033[m - \033[33;7mQUENTE! QUENTE! QUENTE!🔥🔥🔥\033[m
''')
user = 0
tentativas = 0
cor_Palpites = ''
resposta = ''

print('🤖 VOCÊ ESTÁ PRONTO? ')
while resposta != 'S':
    resposta = input('😼 DIGITE S/N: ').strip().upper()
    if resposta == 'S':
        print('🤖 - Okay, vamos lá!!')
        sleep(2)
        os.system('cls') or None
        print('-='*20)
        print('🤖 PENSANDO EM UM NÚMERO... ')
        sleep(3.5)
        
        break
    elif resposta == 'N':
        print('Okay, até a proxima então. 👋')
        sys.exit()
    else: 
        print('Resposta \033[31mInvalida\033[m! TENTE NOVAMENTE.')

while pc != user:
    user = int(input('Digite um \033[34mnúmero\033[m de \033[4m1 a 10\033[m: '))
    if pc != user:

        print("Eita, você errou! Tente novamente.")
        sleep(0.5)
        tentativas += 1
        
        if user+3 == pc or user+2 == pc or user-2 == pc or user-3 == pc:
            cor_Palpites = '\033[33mPALPITES\033[m'
        elif user+1 == pc or user-1 == pc:
            cor_Palpites = '\033[32mPALPITES\033[m'
        else:
            cor_Palpites = '\033[31mPALPITES\033[m'
        
        print(f'Você já deu {tentativas} {cor_Palpites}! ')
        sleep(1.5)
        


print('Você ACERTOU!!!')


