#entrada
prod = input("Informe a distância percorrida em metros: ")
x = float(prod)

des = input("Informe o tempo em segundos: ")
y = float(des)

#processamento
oi = x / y
tchau = oi * 3.6

#saida
print (f'A velocidade média é {oi:.2f} m/s')
print(f'A velocidade média é {tchau:.2f} km/h')