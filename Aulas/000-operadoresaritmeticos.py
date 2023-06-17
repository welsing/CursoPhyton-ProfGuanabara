# + adição
# - subtração
# * multiplicação
# / divisao
# ** potencia
# // divisao inteira
# % resto da divisao 

# ordem de precedencia
# 1 ()
# 2 **
# 3 *, /, //, %
# 4 +, - 


n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma vale {} \n o produto é {} e a divisão é {}'.format(s, m, d))
print('A divisao inteira é {} e a potencia é {}'.format(di, e))

##   raizQ = n ** (1/2) 