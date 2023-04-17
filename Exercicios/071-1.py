# Tentando outra forma de fazer o ex 71
print('#'*30)
print('{:^30}'.format('💸 ATM 💸'))
print('#'*30)
valor = int(input('Digite qual valor deseja sacar R$: '))
total = valor 
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Imprimindo {totced} cédulas de {ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        else: 
            break
        totced = 0
print('='*30)
print('Volte sempre! ')        