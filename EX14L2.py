#entrada de dados
vt = input("Informe o valor a vista da sua fatura: ")
fatura = float(vt)

vp= input("Informe o valor da sua parcela mensal: ")
parcela = float(vp)

#processamento
C = fatura / 10
J = (parcela * 100) / C
J1 = (J - 100) / 100

#saida
print (f'Os juros pagos mensalmente pela sua fatura é: {J1:.1%}')