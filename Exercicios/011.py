b = float(input('-- Qual é a largura da parede? : '))
h = float(input('-- Qual é a altura da parede? : '))
area = b * h

print('--- Sua parede tem a dimensão de {}x{} e sua área é de {}m2. \n Para pintar essa parede, voc precisará de {}L de tinta..'.format(b, h, area, area/2))