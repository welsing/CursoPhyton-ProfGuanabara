# 063 - Escreva um programa que leia um número N inteiro qualquer 
# e mostre na tela os N primeiros elementos de uma sequencia de Fibonacci.
# ex: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8

print('-'*35)
print('SEQUENCIA \033[4mFIBONACCI\033[m')
print('-'*35)
termos = int(input('Quantos termos você quer mostrar?: '))
print('~'*35)

count = 0
ultimo = 1
pnultimo = 0
fn = 0
while count < termos:
    print(pnultimo, end=' -> ')
    pnultimo, ultimo = ultimo, ultimo+pnultimo
   
    
    
    
    count += 1


# n = int(input('A sequência de Fibonacci de: '))
# a, b = 0, 1
# count = 0
# while count < n:
#     print(a, end=', ')
#     a, b = b, a+b
#     count += 1
# print('FIM')