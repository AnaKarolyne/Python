valor = input("Digite o  valor do seu sálario atual: ")
num = float(valor)
valor2 = input("Digite o  valor do seu sálario antigo: ")
num2 = float(valor2)
aumento = (num - num2) / num
print(f'A porcentagem de aumento adquirida foi de {aumento:.2%}')