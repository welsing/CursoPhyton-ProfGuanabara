# While é uma estrutura de repetição de teste logico
impar = par = 0
n = 1
while n != 0:
    n = int(input('Digite um número: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print(f'Você escolhei {par} números pares e {impar} números impares')

# DESAFIOS: 

# 057 - Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores "M" ou "F". 
# Caso esteja errado, peça para digitar novamente até ter um valor correto

# 058 - Melhore o jogo DESAFIO 028 onde o computador vai "PENSAR" em um número entre 0 e 10. 
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites 
# foram necessários para vencer.

# 059 - Crie um programa que leia dois valores e mostre um menu na tela:
# [1] Somar
# [2] Multiplicar
# [3] Maior
# [4] Novos Números
# [5] Sair do programa
# Seu programa deverá realizar a operação solicitada em casa caso.

# 060 - Faça um programa que leia um número qualquer e mostre o seu fatorial
# ex: 5!= 5x4x3x2x1 = 120 (Da pra fazer com while e for)

# 061 - Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, 
# mostrando os 10 primeiros termos da progressão usando a estrutura while

# 062 - Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
#  O programa encerra quando ele disser que quer mostrar 0 termos.

# Escreva um programa que leia um número N inteiro qualquer 
# e mostre na tela os N primeiros elementos de uma sequencia de Fibonacci.
# ex: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8

# 064 - Crie um programa que leia vários números inteiros pelo teclado. 
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. 
# No final, mostre quantos números foram digitados e qual foi a soma entre eles(Desconsiderando o flag)

# 065 - Crie um programa que leia vários números inteiros pelo teclado. 
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. 
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.




