nome = str(input("Me diga seu nome completo: ")).strip()
nomes = nome.split()
print("Seu primeiro nome é {} e seu ultimo nome é {}.".format(nomes[0], nomes[-1]))