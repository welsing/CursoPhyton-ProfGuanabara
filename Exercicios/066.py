# 066 - Crie um programa que leia varios números inteiros pelo teclado. O programa só vai parar quando o usuario digitar o valor 999,
# que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (Desconsiderando o flag)

soma = count = 0
while True:
    n = int(input('Digite um \033[34mnúmero\033[m: '))
    if n != 999:
        soma += n
        count += 1
    if n == 999:
        break
print(f"Você \033[4mdigitou\033[m \033[32m{count}\033[m números\nA \033[4msoma\033[m dos números é \033[32m{soma}\033[m")
