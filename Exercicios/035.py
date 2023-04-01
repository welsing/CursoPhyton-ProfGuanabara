#35 - Desenvolva um programa que leia o comprimento de tres retas e diga ao usuario se elas podem ou não formar um triangulo
# r1 ----
# r2 ------
# r3 ---

print("CALCULAR POSSIBILIDADE DE TRIANGULOS")
a = float(input("Primeiro lado: "))
b = float(input("Segundo lado: "))
c = float(input("Terceiro lado: "))

if (a + b <= c) or (b + c <= a) or (c + a <= b):
    print("Você não pode formar um triangulo com essas retas.")
elif (a == b) and (a == c):
    print("Podemos formar um triangulo equilátero")
elif (a == b) or (a == c) or (b == c):
    print("Podemos formar um tringulo isosceles")
else:
    print("Podemos formar um triangulo escaleno.")
