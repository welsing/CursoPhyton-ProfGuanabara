# 089 - Faça um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a Média de cada um e permita que o usuario possa mostrar 
# as notas de cada aluno individualmente.

from time import sleep

alunosDaEscola = []
alunoCadastro = []
sorn = ''
print("{:^30}".format("CADASTRO DE ALUNOS"))
print('-='*15)
while True:
    alunoCadastro.append(input('Nome: ').title())
    while True:
        try:
            n1 = float(input('Nota 1: '))
            if n1 > 10 or n1 < 0:
                print('Nota \033[31minvalida\033[m, apenas notas de 0 a 10.')
            else:
                break
        except (ValueError):
            print('Nota \033[31minvalida\033[m, tente novamente!')       
    while True:
        try:
            n2 = float(input('Nota 2: '))
            if n2 > 10 and n2 < 0:
                print('Nota \033[31minvalida\033[m31, apenas notas de 0 a 10.')
            else:
                break
        except (ValueError):
            print('Nota \033[31minvalida\033[m, tente novamente!')
    
    alunoCadastro.append(n1)
    alunoCadastro.append(n2)
    alunosDaEscola.append(alunoCadastro[:])
    alunoCadastro.clear()
    while sorn != "N":
        sorn = input('Quer continuar?[S/N]: ').upper().strip()[0]
        if sorn in 'NS':
            print('='*25)
            break
        else:
            print('ESCOLHA \033[31mINVALIDA\033[m! TENTE NOVAMENTE.')
    if sorn == 'N':
        print('CADASTRANDO ALUNOS...')
        sleep(2)
        break
    

print('{:-^40}'.format(' ALUNOS ESCOLA SUN🌞 '))
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>15}')
print('-'*40)
for n, aluno in enumerate(alunosDaEscola):
    print(f"{n:<4}{aluno[0]:<10}{(aluno[1]+aluno[2])/2:>15.1f}  ")
print('='*40)

while n != 999:
    try:
        n = int(input('Checar nota de aluno [999 p/ \033[31msair\033[m]]: '))
    except(ValueError):
        print('ESCOLHA \033[31mINVALIDA\033[m! TENTE NOVAMENTE.')
    if n != 999:
        print(f"As notas de \033[34m{alunosDaEscola[n][0]}\033[m é {alunosDaEscola[n][1:]}")
    print('_'*50)

print('ATÉ LOGO!')
    
