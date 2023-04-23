# 074 - Crie um programa que vai gerar 5 numeros aleatorios e colocar em uma tupla
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
 
from random import randint

tupla = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))

print(f'👨‍💻 Pensei nos números: {tupla}')

print(f'O maior número é {sorted(tupla)[0]}')
print(f'O menor número é {sorted(tupla)[-1]}')