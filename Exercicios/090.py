# 090 - Faça um programa que leia NOTA e MEDIA de um aluno, guardando também a situação(aprovado\reprovado)
# em um DICIONARIO. No final, mostre o conteudo da estrutura na tela

aluno = dict()
print(f"{'CONSULTAR STATUS ESCOLAR':^35}")
aluno['nome'] = input('Nome: ')
aluno['media'] = float(input("MÉDIA: "))
if aluno['media'] > 6:
    aluno['status'] = "APROVADO!"
else:
    aluno['status'] = "REPROVADO!"

print(f'{aluno["nome"].upper()} teve a média de {aluno["media"]} e está {aluno["status"]}')