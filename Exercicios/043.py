#   43 - Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
# calcule o IMC e mostre seu status,
# de acordo com a tabela abaixo:

# - Abaixo de 18.5: Abaixo do peso
# - Entre 18.5 e 25: Peso ideal
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# - Acima de: 40: Obesidade Mórbida
from math import pow

print('''
        \033[7mIMC CALCULATOR 2023\033[m
# - Abaixo de \033[34m18.5\033[m: \033[4mAbaixo do peso\033[m
# - Entre \033[34m18.5\033[m e \033[32m25\033[m: \033[4mPeso ideal\033[m
# - \033[32m25\033[m até \033[33m30\033[m: \033[4mSobrepeso\033[m
# - \033[33m30\033[m até \033[31m40\033[m: \033[4mObesidade\033[m
# - Acima de \033[31m40\033[m: \033[4;35mObesidade Mórbida\033[m \n
''')
peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso/(pow(altura, 2))
print('SEU IMC FICOU EM: {:.2f}'.format(imc))
if imc < 18.5:
    print('Abaixo do peso ideal. \n Busque dietas mais \033[32msaudaveis\033[m e \033[31mproteinas\033[m.')
elif imc > 18.5 and imc < 25:
    print('Você está no \033[32mpeso ideal\033[m.')
elif imc > 25 and imc < 30:
    print('Você está em \033[33msobrepeso\033[m.')
elif imc > 30 and imc < 40:
    print('\033[31mATENÇÃO\033[m, você está em estado de \033[31mobesidade\033[m. \n Procure fazer exercicios fisicos, e se alimentar melhor.')
else:
    print('''\033[31mATENÇÃO!!!\033[m
    Você está em estado de \033[35mObesidade Mórbida\033[m, isto é um estado \033[31mgrave\033[m. Aconselho que procure ajudas \033[4mmedicas\033[m. 
    \033[38mLogo estará melhor\033[m, \033[4;36cuide de sí e de seu futuro.\033[m''')
