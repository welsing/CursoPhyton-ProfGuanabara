# 080 - Crie um programa onde o usuario possa digitar 5 valores númericos e os coloque em uma lista.
# já na posição correta de inserção (Sem usar sort())
# No final, mostre a lista ordenada na tela 


lista = []
for i in range(0,5):
    n = int(input(f'Digite o {i+1}º valor: '))
    if i == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionado no fim da lista...')
    else:
        pos = 0
        while pos <= len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos+1}')
                break
            pos += 1
    print('-'*30)

print(f'valores em ordem: {lista}')    