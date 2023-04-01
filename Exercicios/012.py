## ler preco do produto, e dae 5% de desconto

print('## Olá, sou seu o seu auxiliar para te ajudar calcular desconto para os clientes.')
print('='*20)
print('## Vamos começar cadastrando o cliente.')
name = str(input('Qual nome do cliente? : '))
pname = str(input('Qual nome do produto? : '))
prod = float(input('Qual valor do produto? R$'))
porc = float(input('Quantos % de desconto dara ao cliente? : '))
desc = (porc*prod)/100

print('Okay, para o(a) Sr(a). {} que deseja comprar  {} no valor de R${}, será aplicado um desconto de {}%. o cliente devera pagar R${:.2f}. '
      '\n -- BOAS VENDAS!'.format(name, pname, prod, porc, prod-desc))