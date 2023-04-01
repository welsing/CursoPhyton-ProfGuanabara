####
print('#'*10, 'LOCALIZA ORÇAMENTO','#'*10)


days = int(input('Por quantos dias o carro foi alugado?: '))
km = float(input('Quantos Km foram percorridos com este veiculo?: '))
pgdays =  days * 60.00
pgkm = km * 0.15
total = pgdays + pgkm

print('O veiculo foi alugado por {} dias e percorreu {}Km. \n === TOTAL A PAGAR === \n ----- R${:.2f} \n --- {}km = R${:.2f} \n --- {} dias = R${:.2f}'.format(days, km, total, km, pgkm, days, pgdays))