city = str(input('Nome de uma cidade: '))#.strip()

city = city.lower()
city = city.split()



print('A primeira palavra é Santo? ')
if 'santo' in city[0]:
    print('---- É sim!')
else:
    print('---- Não é!')