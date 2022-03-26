#entrada de dados
valor = input("NAC: ")
nac = float(valor)

valor = input("AM: ")
am = float(valor)

valor = input("PS: ")
ps = float(valor)

#processamento
media = (2 * nac + 3 * am + 5 * ps) / 10

#saida
print("A média vale", media)