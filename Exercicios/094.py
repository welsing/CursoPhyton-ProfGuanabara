# 094 - Crie um programa que leia NOME, SEXO E IDADE de varias pessoas, guardando os dados de cada pessoa
# em um DICIONARIO e todos os dicionarios em uma lista. No final, mostre:
# a) Quantas pessoas foram cadastradas.
# A MEDIA DE IDADE
# b) Uma lista com nome das mulheres.
# c) Uma lista com todas as pessoas com idade ACIMA da média. 

pessoas = list()
media = 0
mulheres = list()
while True:
    print('-->> CADASTRO DE PESSOA <<--') 
    cadastroPessoa = { 'NOME':input('Nome: ').title().strip(), 
                       'SEXO':input('Sexo [M/F]: ').upper().strip()[0],
                       'IDADE':int(input('Idade: ')) }
    pessoas.append(cadastroPessoa.copy())
    sorn = input('Quer continuar? [S/N]: ').upper().strip()[0]
    if sorn == 'N':
        break
for i, p in enumerate(pessoas):
    if pessoas[i]['SEXO'] == 'F':
        mulheres.append(pessoas[i]['NOME'])
    media += pessoas[i]['IDADE']
media = media/len(pessoas)
print('-='*10)
print(f'Pessoas cadastradas: {len(pessoas)}')
print(f'Média de idade: {media:.0f}')
print(f'Mulheres Cadastradas: {mulheres}')
print(f'Pessoas acima da média: ', end='')
for i, p in enumerate(pessoas):
    if pessoas[i]['IDADE'] > media:
        print(pessoas[i]['NOME'], end=' | ')
