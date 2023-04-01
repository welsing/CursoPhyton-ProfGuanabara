# tem um produto, se pagar a vista tem % de desconto, se parcelar tem % de aumento

print('-- ORÇAMENTO DE PRODUTOS')
cname = str(input('Seu nome: '))
pname = str(input('Qual produto deseja?: '))
valor = float(input('Qual valor do produto? R$'))
desc = valor - ((valor*10)/100)
acres = valor + ((valor*20)/100)

print('Olá, Sr(a). {}. Irei te passar o orçamento para {}.\n -- VALOR BRUTO: R${} \n VALOR À VISTA C/ 10% DE DESC: R${:.2f} \n VALOR PARCELADO C/ 20% DE JUROS: R$ {:.2f}'.format(cname, pname, valor, desc, acres))

