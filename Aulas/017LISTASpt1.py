# Nas listas, diferente das tuplas, os itens são mutaveis, podendo aplicar por exemplo:
# lista[3] = 'mudando item'
# Ou adicionar itens no final utilizando:
# lista.append('Novo Item')
# ou em alguma parte, utilizando: 
# lista.insert(2, 'novo item')

# Uma maneira de apagar seria utilizando o comando Del, não é uma função nem um metodo.
# ex: del lista[3]
# ou utilizando o metodo pop
# lanche.pop(3)
# Se usar lanche.pop() ele apaga o ultimo elemento
# ou o Remove pelo valor e não pela chave.
# lanche.remove('Apagar Item')

# Para ordenar itens podemos usar o metodo sort()
# lista.sort() e podemos adicionar reverse=True

# Se vc faz a lista se igualar a outra lista, o phyton não copia a lista para outra var, ele cria uma ligação
# ex: novaLista = Lista 
# para resolver isso use 
# novaLista = lista[:]
# sendo [:] receber TODOS os valores


lista = [1,8,11,23]
lista.remove(11)
lista.insert(2, 15)
lista.sort(reverse=True)
lista.pop(0)
print(lista)
print(f'Minha lista tem {len(lista)} elementos')

print('PROXIMA LISTA\n')

valores = []
for insert in range(0,5):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'Na posição {c+1} encontrei {v}...')


# DESAFIOS 

# 078 - Faça um programa que leia 5 VALORES NÚMERICOS e guarde-os em uma lista
# No final, mostrel qual foi o maior valor e o menor  valor digitados e suas respectivas posições na lista.

# 079 - Crie um programa onde o usuario possa digitar, varios valore númericos, e cadastre em uma lista.
# Caso o número já exista la dentro, ele não será adicionado.
# No final, será exibido todos os valores únicos em ordem CRESCENTE. 

# 080 - Crie um programa onde o usuario possa digitar 5 valores númericos e os coloque em uma lista.
# já na posição correta de inserção (Sem usar sort())
# No final, mostre a lista ordenada na tela 


# 081 - Crie um programa que vai ler varios números e colocar numa lista. 
# Depois disso mostre:
# a) Quantos números foram digitados
# b) A lista de valores, ordenada de forma decrescente
# c) Se o valor 5 foi digitado e está ou não na lista.

# 082 - Crie um programa que vai ler varios números e colocar numa lista. 
# Depois disso, crie duas listas extras que vão conter apenas valores pares
# e os valores imparas digitados, respectivamente
# No final mostre o conteudo das 3 listas geradas. 

# 083 - Crie um programa onde o usuario digite uma expressão qualquer que use parenteses. 
# Seu aplicativo deverá analisar se a expressão passada está com parenteses abertos e fechados na ordem correta.









