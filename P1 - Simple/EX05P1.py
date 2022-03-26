#Fazer um algoritmo que ao receber o salário atual de um funcionário, calcule o valor do novo salário reajustado de acordo com a tabela abaixo:
#Salário atual	Reajuste
#Abaixo de R$500,00	15%
#de R$500,00 até R$1000,00	10%
#Acima de R$1000,00	5%

print("Rajuste salarial")
sal = float(input("Qual é o seu salário atual? "))

if (sal<500):
    sn1 = sal * 0.15
    sn11 = sn1 + sal
    print(f'O reajuste salarial esperado para esse ano é de R$ {sn1:.2f}')
    print(f'Assim sendo, você passará a receber R$ {sn11:.2f}')

elif (sal>=500) and (sal<1000):
    sn2 = sal * 0.10
    sn22 = sn2 + sal
    print(f'O + reajuste salarial esperado para esse ano é de R$ {sn2:.2f}')
    print(f'Assim sendo, você passará a receber R$ {sn22:.2f}')

else:
    sn3 = sal * 0.05
    sn33 = sn3 + sal
    print(f'O - reajuste salarial esperado para esse ano é de R$ {sn3:.2f}')
    print(f'Assim sendo, você passará a receber R$ {sn33:.2f}')

