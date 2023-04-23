# 077 -  Crie um prorama que tenha um tupla com várias palavras(não usar acentos) 
# Depois disso, você deve mostrar, para cada palavra, quais são suas vogais

tupla = ('Beck', 'Maconha', 'Weed', 'Balazul', 'Seda', 'Bong', 'Piper', 'Dixava', 'Isquero')

for i in range(0, len(tupla)):
    print(f'Na palavra \033[34m{tupla[i].upper()}\033[m temos -> ', end='')

    for v in range(0, len(tupla[i])):
        palavra = tupla[i][v]
        if palavra.lower() in 'aeiou':
            print(f'{palavra}', end=' ')
    print('')
print('\033[31mAcabou!\033[m')


