salario = int(input("Digite o valor do salario: R$: "))
desc_Caju = int(input("Digite quantos % de desconto do caju: "))
desc_Plano = int(input('Digite quantos % de desconto do plano de saúde e odonto: '))

porc_Caju = (salario*desc_Caju)/100
porc_Plano = (salario*desc_Plano)/100

print(f"Do seu salario de R${salario} será descontado\n - R${porc_Caju} do CAJU  \n - R${porc_Plano} do plano de saúde e Odontologico")
print(f'Seu salario total será: R${(salario-porc_Caju) - porc_Plano}')