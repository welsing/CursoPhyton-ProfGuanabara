# Help
# Existe a função help() no phyton, que você pode ler a doc de uma função diretamente no console
# ex: help(print)
# Também podemos saber a doc desse metodo utilizando o  __doc__
# ex: print(print.__doc__) faz a mesma coisa q help(print) só q com outra formatação

## Dicas e regras do def

# Quando temos uma variavel a=10, no nosso programa, na função "a" também será a=10
# pois "a" é uma variavel global, porem, se eu declarar a=5 dentro do escopo do def, "a" sera a=5 apenas para função
# no global "a" continua a=10.
# oq declaro dentro do Def, é uma variavel local
# oq declaro no programa, é uma variavel global
# ex:
def função():
    a = 5
    print(f'a dentro vale: {a}')   # dentro vale 5 
    # porem se coloco algo declarado só fora, e não foi declarado aqui dentro
    print(f'n dentro vale: {n}')  # dentro vale 3 também 

# PROGRAMA PRINCIPAL ⬇️
a = 10
print(f'a fora vale: {a}') # fora vale 10
n = 3
print(f'n fora vale: {n}') # fora vale 3 

# Uma forma de fazer a função manipular a variavel global é utilizando o "global" dentro da função
# assim a função vai fazer com que aquela variavel declarada seja GLOBAL e passe valer o valor definido DENTRO dela
# Ex:
def função():
    global a
    a = 8
    print(f'a dentro vale: {a}') ## dentro vale 8
# PROGRAMA PRINCIPAL ⬇️
a = 5
função()
print(f'a fora vale: {a}') ## Fora TAMBÉM vai valer 8, pois a função modificou a variavel