## ler salario de um funcionario e dar 15% de aumento.

print('×'*10, 'BossSimulator3000', '×'*10)

s = float(input('Quanto voc ganha atualmente? R$'))
porc = int(input('Quanto % quer de aumento? R$'))
aum = (s*porc)/100

print('#'*30)
print('-- Parabéns, voce mereceu e hoje estamos te dando um aumento de {}%, vimos que seu salario é de R${}.\n #### O seu salario atualizado ficará em R${:.2f}'.format(porc, s,s+aum))