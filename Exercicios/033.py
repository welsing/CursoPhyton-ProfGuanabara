#33 - Faça um programa que leia tres numeros e mostre qual é o maior e qual é o menor

n1 = int(input("Me diga um numero: "))
n2 = int(input("Outro numero: "))
n3 = int(input("Mais um: "))

'''if n1 > n2 and n1 > n3:
    print("O maior numero é {}".format(n1))
elif n2 > n3 and n2 > n1:
    print("O maior numero é {}.".format(n2))
elif n3 > n2 and n3 > n1:
    print("O maior numero é {}.".format(n3))
else:
    print("Os números são iguais! ") '''

# Verificando o menor.
menor = n1
if n2<n1 and n2<n3:
    menor = n2
if n3<n1 and n3<n2:
    menor = n3
# Verificando maior
maior = n2
if n1>n2 and n1>n3:
    maior = n1
if n3>n1 and n3>n2:
    maior = n3

print("O maior é: {} \n O menor é: {}".format(maior, menor))
