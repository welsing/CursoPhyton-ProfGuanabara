# 076 - Crie um programa que tenha um tupla unica com nome de produtos e seus respectivos preços
# no final, mostre uma listagem de preços, organizando os dados em forma tabular

produtos = ('Anel', 35.75, 'Bag', 180.00, 'Blusa High', 219.99, 'Calça Cargo', 300.00, 'Vans sk8 Hi', 449.90, 'Meias VANZ', 40.00, 'Jaqueta Jeans', 399.70)

print('='*40)
print('{:^40}'.format('Lojas Crazy'))
print('='*40)
for i in range(0, len(produtos), 2):
    preço = produtos[i+1]
    print('{:.<30}'.format(produtos[i]), f'R$:{preço}')
    



