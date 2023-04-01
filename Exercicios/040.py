# 40 - Crie um programa que leia duas notas de um aluno e calcule sua média,
# mostrando uma mensagem no final, de acordo com a media atingida:

# - Média abaixo de 5.0: REPROVADO
# - Média entre 5 e 6.9: RECUPERAÇÃO
# - Média acima de 7.0: APROVADO

name = input('Olá, vamos calcular sua média nesse bimestre. \n Primeiro, me diz seu nome: ')

n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
media = (n1+n2)/2

if media >= 7:
 print('Parábens, \033[34m{}\033[m você foi \033[32;1mAPROVADO\033[m! '
       '\n Sua média foi \033[33m{}\033[m'.format(name, media))
elif 6.9 > media >= 5:
 print(' Você está de \033[33;1mRECUPERAÇÃO\033[m! Bom, {} não foi reprovado porem precisa estudar mais. \n '
       '\n Sua média foi \033[33m{}\033[m'.format(name, media))
else:
 print('Você está \033[31mREPROVADO\033[m! Que pena, você não passou. Tente novamente ano que vem.'
       '\n Sua média foi \033[33m{}\033[m'.format(media))