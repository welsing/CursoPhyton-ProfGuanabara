import random


print('*Aula do Prof.º Gerald* \n - Chegamos ao fim da aula, entre 4 alunos irei decidir quem apagará o quadro e ganhará um chocolate.')
print(' - Escrevam seu nome e vamos sortear.')

a = input('1º Aluno: ')
b = input('2º Aluno: ')
c = input('3º Aluno: ')
d = input('4º Aluno: ')
alunos = [a, b, c, d]
aluno = random.choice(alunos)

print('Os alunos que se inscreveram foram: {}, {}, {} e {}. \n O nosso grande escolhido é {}. Parábens.'.format(a,b,c,d,aluno))



