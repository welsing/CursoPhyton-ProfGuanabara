# 081 - Crie um programa que vai ler varios números e colocar numa lista. 
# Depois disso mostre:
# a) Quantos números foram digitados
# b) A lista de valores, ordenada de forma decrescente
# c) Se o valor 5 foi digitado e está ou não na lista.


lista = []
while True:
    while True:
        try:
            n = int(input('Digite um número: '))
            break
        except ValueError:
            print('Elemento invalido! ')
    lista.append(n)
    while True:
        sorn = input("Quer continuar? [\033[34mS/N\033[m]: ").strip().upper()[0]
        if sorn in 'SN':
            break
        else:
            print('Escolha \033[31minvalida\033[m!')
    if sorn == 'N':
        print('#'*25)
        break
    print('='*25)

print(f'Foram digitados {len(lista)} números.')
if 5 in lista:
    print('O valor 5 foi digitado e \033[32mestá\033[m na lista.')
else: 
    print('O valor 5 \033[31mnão\033[m está na lista.')
lista.sort(reverse=True)
print(f'Números em forma \033[34mdecrescente\033[m: \n {lista}')
    
            





