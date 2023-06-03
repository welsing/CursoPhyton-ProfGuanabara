# 090 - Faça um programa que leia NOTA e MEDIA de um aluno, guardando também a situação(aprovado\reprovado)
# em um DICIONARIO. No final, mostre o conteudo da estrutura na tela

aluno = dict()
print(f"{'CONSULTAR STATUS ESCOLAR':^35}")
aluno['nome'] = input('Nome: ')
aluno['media'] = float(input("MÉDIA: "))
if aluno['media'] >= 6:
    aluno['status'] = "APROVADO!"
elif 6 > aluno['media'] >= 4:
    aluno['status'] = 'RECUPERAÇÃO'
else:
    aluno['status'] = "REPROVADO!"
print('='*30)
for k, v in aluno.items():
    print(f' - {k} é igual a {v}')
