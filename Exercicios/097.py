# 097 - Faça um programa que tenha a função chamada escreva(), que receba um texto qualquer como parametro
# e mostre uma mensagem com tamanho adaptavel
# ex: escreva('OLÁ MUNDO')
# saida:
# ~~~~~~~~~~~~~
#   OLÁ MUNDO
# ~~~~~~~~~~~~~

def escreva(msg):
    msg = msg.strip()
    print('~'*(len(msg)+6))
    print(f'   {msg}')
    print('~'*(len(msg)+6))

escreva('CURSO EM VIDEO by: Gustavo Guanabara')