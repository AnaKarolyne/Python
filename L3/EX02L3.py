#Escrever um algoritmo que leia dois valores inteiro distintos e informe qual é o maior ou se houve um empate.
a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))

if (a > b):
    print(f'O primeiro número ({a:.1f}) é maior que o segundo ({b:.1f}) número.')

elif (b > a):
    print(f'O segundo número ({b:.1f}) é maior que o primeiro ({a:.1f}) número.')

else: 
    print(f'O primeiro número ({a:.1f}) é igual ao segundo ({b:.1f}) número.')
