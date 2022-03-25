#entrada
prod = input("Informe o valor original do produto: ")
x = float(prod)

des = input("Informe o porcentual referente ao desconto/aumento que devera ser calculado: ")
y = float(des)

#processamento
porcentagem = y / 100
valor = (y * x) / 100

#saida
print("O valor referente ao desconto/aumento será de: ", valor)
print("O valor com o aumento será de: ", (x + valor)) 
print("O valor com o desconto será de: ", (x - valor))