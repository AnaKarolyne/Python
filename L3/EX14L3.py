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

#Fevereiro
elif (m == 2):
    if (a % 400 == 0) or ((a % 4 == 0) and (a % 100 != 0)): 
        if (d <= 29):
            print ('Esse ano é bissexto')
        valida = True 
    elif (d <= 28):
        valida = True  


if (a % 400 == 0) or ((a % 4 == 0) and (a % 100 != 0)):       
    print ('Esse ano é bissexto')
else:
    print ('O ano não é bisssexto.')


if(valida):
    print('Essa data existe, seja feliz!')
else:
    print('Volte no tempo e crie uma data nova, pois essa não existe!')