'''#022 - Crie um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras maiusculas

- O nome com todas as minúsculas

- Quantas letras ao todo (Sem considerar espaçoes)

- Quantas letras tem o primeiro nome.'''


name = str(input('Me diga seu nome completo:')).strip()

print('O nome todo maiusculo ficaria {}.'.format(name.upper()))
print('O nome todo minusculo ficaria {}'.format(name.lower()))
# namespace = name.replace(" ", "")      ---- Pedi para repor os espaços por 0espaços e depois pedi pra contar
# print('O nome sem os espaços tem {} letras.'.format(len(namespace)))
print('O nome tem {} letras.'.format(len(name) - name.count(' ')))     #Pedi pra contar o nome menos os espaços
#fname = name.split()    ------ Separei a string em uma lista depois pedi pra contar o primeiro item
#print('O primeiro nome é {} apenas contem {} letras'.format(fname[0], len(fname[0])))
print('Seu primeiro contem {} letras'.format(name.find(' ')))   # -- Pedi pra contar as letras até o primeiro espaço

