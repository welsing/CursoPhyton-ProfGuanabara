# 082 - Crie um programa que vai ler varios números e colocar numa lista. 
# Depois disso, crie duas listas extras que vão conter apenas valores pares
# e os valores imparas digitados, respectivamente
# No final mostre o conteudo das 3 listas geradas. 

lista_Geral = []
lista_Par = []
lista_Impar = []

while True:
    n = int(input('Digite um \033[34mnúmero\033[m: '))
    lista_Geral.append(n)
    while True:
        sorn = input("Deseja Continuar? [S/N]: ").lower().strip()[0]
        if sorn in 'sn':
            break
        else:
            print("Opção \033[31minvalida\033[m! Tente novamente.")
    print('='*25)
    if sorn == 'n':
        break

for i in lista_Geral:
    if i % 2 == 0:
        lista_Par.append(i)
    else:
        lista_Impar.append(i)

print(f'Todos \033[34mnúmeros\033[m digitados:\n {lista_Geral}')
print(f'Números \033[34mPares\033[m digitados:\n {lista_Par}')
print(f'Números \033[34mImpares\033[m digitados:\n {lista_Impar}')
