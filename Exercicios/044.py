# 44 - Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:

# - À VISTA DINHEIRO/CHEQUE: 10% de desconto
# - À VISTA NO CARTÃO: 5% de desconto
# - EM ATÉ 2X NO CARTÃO: Preço Normal
# - 3X OU MAIS NO CARTÃO: 20% de juros
import random
print('''
       \033[41mLOJA AMERICANAS\033[m
        \033[4;37mTodo mundo vai.\033[m
- Olá, senhor. deseja comprar algum produto?''')

# valor = random.randint(30, 800) ## Randomizar valor
valor = float(input('Insira valor'))

resposta = input('Escolha S/N:').upper()
if resposta == 'S':
    print(' - Perfeito! Vamos começar. A proposito, qual seu nome?')
    nome = input('\033[7mDigite seu nome:\033[m ')
    print(' - Legal, \033[34;4m{}\033[m. Qual produto você tem interesse? vamos fazer uma \033[4msimulação\033[m.'.format(nome))
    print(' - Primeiro, me diga o nome do produto que deseja simular.')
    produto = input('\033[7mDigite o nome do produto:\033[m ')
    print(' - Legal, parece que temos sim \033[32m{}\033[m em estoque! '
          '\n Atualmente ele está em \033[4mpromoção\033[m saindo por apenas \033[32mR$:{},99\033[m!\n '
          '\n \033[4mVamos escolher sua opção de pagamento.\033[m'.format(produto, valor))
    print('''[1] - À VISTA DINHEIRO/PIX: \033[32m10% de desconto\033[m
[2] - À VISTA NO CARTÃO: \033[32m5% de desconto\033[m
[3] - EM ATÉ 2X NO CARTÃO: \033[33mPreço Normal\033[m
[4] - 3X OU MAIS NO CARTÃO: \033[31m20% de juros\033[m''')
    opcao = int(input('\033[7mDIGITE A OPÇÃO DE PAGAMENTO:\033[m '))
    if opcao == 1:
        print('- Ótima escolha, à vista o valor do produto será de \033[32mR$:{}\033[m.'.format(valor-(valor*10/100)))
    elif opcao == 2:
        print('- Perfeito! à vista no cartão com 5% de desconto o você pagará \033[32mR$:{}\033[m.'.format(valor-(valor*5/100)))
    elif opcao == 3:
        print('- Okay, em 2x no cartão você pagará o preço normal. \033[32mR$:{}\033[m.'.format(valor))
    elif opcao == 4:
        print('- Boa escolha, vamos parcelar sua compra e com os \033[31m20% de juros\033[m o valor total será de \033[32mR$:{}\033[m.'.format(valor+(valor*20/100)))
    else:
        print('Não quer escolher ent vai tomar no cu tchau.')
    print('\033[4mObrigado pela preferencia\033[m, \033[34m{}\033[m! Volte sempre.'.format(nome))


elif resposta == 'N':
    print('- Que pena! Então até logo!')

else:
    print('Resposta invalida.')

