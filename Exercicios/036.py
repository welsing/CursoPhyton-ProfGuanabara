# 36 - Escreva um programa para aprovar o empréstimo bancário para a compra
# de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
#     Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário
# ou então o emprestimo será negado


valor_casa = float(input('Qual valor da casa desejada? R$: '))
salario = float(input('Qual seu salário? R$: '))
anos = int(input('Em quantos anos deseja quitar?: '))
s_porce = salario * 30 / 100
prestacao = (valor_casa / anos) / 12

if prestacao > s_porce:
    print(f'Para pagar uma casa de R${valor_casa:.2f} em {anos} anosa prestação seria de R${prestacao:.2f}')
    print('Infelizmente seu financiamento \033[1;31mNÃO\033[m foi aprovado! :(')
else:
    print('EMPRESTIMO \033[4;32mAPROVADO\033[m!')
    print('Você ira pagar \033[1;34m{}\033[mx de \033[33mR$\033[m\033[4;32m{:.2f}\033[m.'.format(anos * 12, prestacao))
print('\033[7mWelsingBANK\033[m, seu parceiro \033[34mdigital\033[m!')
