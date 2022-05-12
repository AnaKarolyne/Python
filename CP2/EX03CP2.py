from __future__ import division


cedula = int(input("Digite o valor da cédula: "))
primeiraMoeda = int(input("Digite o valor de uma moeda: "))
segundaMoeda = int(input("Digite o valor da outra moeda: "))


restoPrimeiraMoeda = cedula % primeiraMoeda
restoSegundaMoeda = cedula % segundaMoeda
divisaoPrimeiraMoeda = cedula // primeiraMoeda
divisaoSegundaMoeda = cedula // segundaMoeda
soma = (((restoPrimeiraMoeda * primeiraMoeda) + (restoSegundaMoeda * segundaMoeda)) == cedula)
primeiroCaso = ((divisaoPrimeiraMoeda * primeiraMoeda) == cedula)
segundoCaso = ((divisaoSegundaMoeda * segundaMoeda) == cedula)

if soma or primeiroCaso or segundoCaso:
    if soma:
        print("Possível: {:.0f} moeda(s) de {:.0f} e mais {:.0f} moeda(s) de {:.0f}".format(restoPrimeiraMoeda, primeiraMoeda, restoSegundaMoeda, segundaMoeda))
    elif primeiroCaso and segundoCaso:
        print("Possível:  {:.0f} moeda(s) de {:.0f} ou {:.0f} moeda(s) de {:.0f}".format(divisaoPrimeiraMoeda, primeiraMoeda, divisaoSegundaMoeda, segundaMoeda))

else:
    print("Não é possível fazer a troca!")