## FUNÇÕES

# Já utilizamos funções no phyton desde o inicio das aulas, como exemplo: print(), len(), int(), input()
# Essas são funções que já vem no phyton. 

# Uma função é uma forma de simplificar uma rotina, diminuir a quantidade de repetições de codigos.
# Para criarmos uma função no phyton utilizamos o comando ' def ', que basicamente é Definir Função.

# A estrutura é simples.
# def nomeDaFunção(Parametros):    
#   aqui dentro colocamos codigos que a função vá retornar
#   os parametros é caso o codigo que a função retorna precisar de especificar algum valor.

# Obs: O phyton pede que pule 2 linhas após as def, apenas por questão de estrutura.


print('---------- EXEMPLO 1 --------------')
# FUNÇÃO DE PRINTAR LINHA
def linha():
    print('-'*30)

# utilizando a função
linha()

print('---------- EXEMPLO 2 --------------')
# FUNÇÃO DE PRINTAR CABEÇALHO
def cabeçalho(msg):
    linha()
    print(f"{msg:^30}")
    linha()

# Executando a função, note que passamos o parametro msg
cabeçalho('FUNÇÕES PHYTON')
cabeçalho('DOMINE O MUNDO')
cabeçalho('PHYTON É DEMAIS')

## CRIANDO FUNÇÃO DE SOMA
# É muito chato quando fazemos 
# a = 5
# b = 3
# s = a + b
# print(s)

print('---------- EXEMPLO 3 --------------')
# podemos simplificar isso tudo definindo uma função e passando parametros.
def soma(a, b):
    s = a+b
    print(f'A soma de {a} + {b} é {s}')


soma(5, 3)
# QUE ADIANTO NÉ


# E se quisermos adicionarmos mais parametros do que se pode, por exemplo, na função acima se adicionar
# soma(5, 6, 3)
# Vemos que o terceiro parametro não existe, e o phyton nos retornaria um erro.
# para dizer ao phyton que uma função recebe quantos valores forem necessarios, utilizamos "*" 
# como forma de concatenar

print('---------- EXEMPLO 4 --------------')
def contador(*num):
    print(num)

contador(3, 6, 4, 3)
contador(3, 3, 3)

print('---------- EXEMPLO 5 --------------')
# Vamos por mais um exemplo, vamos supor que temos uma lista no programa
valores = [3, 4, 5, 7]

# e no programa precisamos pegar listas com valores, e dobrar eles sempre, por exemplo, 3 viraria 6 e assim vai
# Podemos criar uma função que faça isso
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1
    print(lst)

dobra(valores)

### DESAFIOS ###

# 096 - Faça um programa que tenha uma função chamada area(), que receba as dimensões de um terreno retangular
# (largura e cumprimento) e mostre a area do terreno.

# 097 - Faça um programa que tenha a função chamada escreva(), que receba um texto qualquer como parametro
# e mostre uma mensagem com tamanho adaptavel
# ex: escreva('OLÁ MUNDO')
# saida:
# ~~~~~~~~~~~~~
#   OLÁ MUNDO
# ~~~~~~~~~~~~~

# 098 - FAça um programa que tenha uma função chamada contador(), que receba tres parametros: 
# Inicio, fim e passo e realize a contagem. Seu programa tem que realizar 3 contagens atraves da função criada.
# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) Uma contagem personalizada
 
# 099 - Faça um programa que tenha uma função chamada maior(), que receba varios parametros de valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

# 100 - Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somarPar()
# A primeira função vai sortear 5 números e vai coloca-los dentro da lista e a segunda função vai mostrar
# a soma entre todos os valores pares sorteados pela função anterior.


