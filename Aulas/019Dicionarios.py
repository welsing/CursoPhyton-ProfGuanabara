# DICIONARIOOS

## exemplo 
# pessoas = {'nome':'bernardo','idade':'21'}
#              key   values
# para acessar: pessoas['key']
# vai aparecer: value

# para saber quais são as keys de um dicionario 
# pessoas.keys()

# para saber os valores de um dicionario 
# pessoas.values()

# Se quiser saber o keys + values
# pessoas.items()
# no for não usamos enumerate(), usamos o .items()

# para adicionar algo ao dicionario não usamos .append()
# apenas o declaramos e ele cria a key e coloca o valor
# pessoas['sexo'] = 'M'
# --> pessoas = {'nome':'bernardo','idade':'21', 'sexo':'M'}
# para alterar é a mesma logica.

# para remover: del pessoas['idade']
# --> pessoas = {'nome':'bernardo','sexo':'M'}

# PODEMOS CRIAR UM DICIONARIO DENTRO DE UMA LISTA!

# para usar o .append de um dicionario para um lista, não podemos usar o fatiamento [:]
# por isso existe o metodo .copy()
# lista = list()
# lista.append(pessoas.copy())

# EXERCICIOS

# 090 - Faça um programa que leia NOTA e MEDIA de um aluno, guardando também a situação(aprovado\reprovado)
# em um DICIONARIO. No final, mostre o conteudo da estrutura na tela

# 091 - Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatorios. 
# guarde esses resultados em um dicionario. No final, coloque esse dicionario em ordem, sabendo que
# o vencedor tirou o maior numero no dado.

# 092 - Crie um programa que leia NOME, ANO de NASC., e CARTEIRA DE TRABALHO e cadastre-os (com idade)
# em um DICIONARIO. se por acaso a CTPS for diferente de 0, o dicionario receberá também o ano da contratação
# e o salario. Calcule e acrescente, alem da idade, com quantos anos a pessoa vai se aposentar.

# 093 - Crie um programa que gerencie o aproveitamento de um JOGADOR DE FUTEBOL. O programa vai
# ler o NOME DO JOGADOR e QUANTAS PARTIDAS ele jogou. depois vai ler a QUANTIDADE DE GOLS feitos em cada partida
# No final, tudo isso será guardado em um dicionario, incluindo o total de gols feitos durante o dicionario.

# 094 - Crie um programa que leia NOME, SEXO E IDADE de varias pessoas, guardando os dados de cada pessoa
# em um DICIONARIO e todos os dicionarios em uma lista. No final, mostre:
# a) Quantas pessoas foram cadastradas.
# A MEDIA DE IDADE
# b) Uma lista com nome das mulheres.
# c) Uma lista com todas as pessoas com idade ACIMA da média. 

# 095 - Aprimore o desafio 93 para que ele funcione com varios jogadores. incluindo um sistema de visualização
# de detalhes de aproveitamento de cada jogador.

