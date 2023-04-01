from math import radians, sin, cos, tan
ang = float(input('Me informe um angulo:'))
sen = sin(radians(ang))
cos = cos(radians(ang))
tg = tan(radians(ang))

print('### ANALISE DO ANGULO DE {:.2f}º ### \n - SENO = {:.2f} \n - COSSENO = {:.2f} \n - TANGÊNTE = {:.2f}'.format(ang, sen, cos, tg))
