#input de dados
d = int(input("Dia: "))
m = int(input("Mês: "))
a = int(input("Ano: "))
valida = False

#Meses com 31 dias
if (m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m ==12):
    if (d <= 31):
        valida = True
        #Meses com 30 dias 
elif (m == 4 or m == 6 or m == 9 or m == 11):
        if (d <= 30):
                valida = True
elif (m == 2):
    if (d == 28):
        valida = True

if(valida):
    print('Data válida')
else:
    print('Inválida')
