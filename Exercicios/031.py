# 31 - desenvolva um mprograma que pergunte a distancia de uma viagem em km.
# calcule o preço da passagem, cobrando $0,50 por km para viagens até 200km e $0,45 para viagens mais longas


print("Bem vindo ao \033[34;4mOnBus\033[m, vamos simular o preço da sua viagem?")
print("Nossos preços dependem da kilometragme das viagem, a cada km cobramos $\033[32m0,50\033[m.\n "
      "se a viagem for maior do que \033[4;31m200km\033[m então temos uma \033[42mpromoção\033[m e cada km fica a $\033[32m0.45\033[m")
km = float(input("De quantos KM é sua viagem?: "))
preco = km * 0.50 if km <= 200 else km * 0.45
print("Sua viagem foi de \033[4;31m{:.1f}km\033[m e o preço será de R$\033[32m{:.2f}\033[m".format(km, preco))
''' if km <= 200:
    print("Sua viagem foi de {:.1f}km. "
          "\n ----o valor total fica em R${:.2f}".format(km, km*0.50))
else:
    print("Sua viagem foi de {:.1f}km. temos uma promoção para essa viagem! "
          "\n ----o valor total fica em R${:.2f}".format(km, km * 0.45)) '''

