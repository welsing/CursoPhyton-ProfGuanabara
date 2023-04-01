#42 - Refaça o desafio dos triangulos, acrescentando o recurso de mostrar que
# tipo de triangulo será:
# - Equilátero: Todos os lados iguais
# - Isósceles: Dois lados iguais
# - Escaleno: Todos os lados diferentes.
while True:
    print('\033[33;7mCALCULADORA DE TRIANGULO?\033[m')

    l1 = float(input('Me fale um lado: '))
    l2 = float(input('Outro lado: '))
    l3 = float(input('Mais um: '))

    if l1 < l2+l3 and l2 < l1+l3 and l3 < l1+l2:
        print('Podemo formar um triangulo ', end='')
        if l1 == l2 == l3:
            print('\033[34mEQUILÁTERO\033[m!')
        elif l1 != l2 != l3 != l1:
            print('\033[34mESCALENO\033[m!')
        else:
            print('\033[34mISOSCELES\033[m!')
    else:
        print('Você \033[31mNÃO\033[m pode formar um triangulo com essas medidas.')


    # Codigo que eu fiz, mas vou refazer acima de outra forma.
    # if l1+l2 > l3 and l1+l3 > l2 and l2+l3 > l1:
    #     print('\033[32mOkay\033[m temos um triangulo')
    # else:
    #     print('\033[31mNão\033[m é possivel formar um \033[4mtriangulo\033[m com essas medidas.')
    #     break
    # if l1 == l2 and l2 == l3 and l1 == l3:
    #     print('Nosso \033[4mtriangulo\033[m é \033[34mEquilatero\033[m!')
    # elif l1 == l2 or l1 == l3 or l2 == l3:
    #     print('Nosso \033[4mtriangulo\033[m é \033[34mIsósceles\033[m!')
    # else:
    #     print('Nosso \033[4mtriangulo\033[m é \033[34mEscaleno\033[m')
    # break




