print('##### Oi, sou o TestCalculator2000! \n ##### Estou aq pra calcular a media de sua nota.')
print('#' * 50)

n1 = float(input('---- Nota da prova 1: '))
n2 = float(input('---- Nota da prova 2 : '))
m = (n1 + n2)/2

print('='*50)
print('#'*20, ' CALCULANDO ', '#'*20)
print('# Voc tirou {} na primeira prova e {} na segunda! \n sua media é {:.2}.'.format(n1, n2, m))

if m > 5 or m == 7:
    print('<<Parabéns, você foi \033[1;32mAPROVADO\033[m!')
else:
    print("Que pena, você foi \033[31;1mREPROVADO\033[m. \n \033[4mEstude mais!\033[m ")
