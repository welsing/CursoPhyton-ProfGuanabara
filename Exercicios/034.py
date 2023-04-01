#34 - Escreva um programa que pergunte o salario de um  funcionario e calcule o valor do seu amento.
#para salarios superiores a 1.250,00 calcule um aumento de 10%
#para inferiores ou iguais o aumento é de 15%

salario = float(input("Qual seu salario?: R$"))

if salario > 1250:
    dez = salario*10/100
    print("Seu salario de R${} passara por um aumento de 10%. \n seu novo salario é de R${}.".format(salario, dez+salario))
else:
    quinze = salario*15/100
    print("Seu salario de R${} passará por um aumento de 15%. \n seu novo salario é de R${}".format(salario, quinze+salario))