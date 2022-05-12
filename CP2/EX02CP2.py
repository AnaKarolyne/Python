#Entrada de dados
vn = float( input("Valor novo: R$ ") )
vv = float( input("Valor original: R$ ") )

#Operação
s = vn - vv
p1 = s * 100
p2 = p1 / vv

#Saída
print("O aumento do produto em reais foi de R$:", s ,)
print("E o seu aumento porcentual (%) foi de", p2,"%")