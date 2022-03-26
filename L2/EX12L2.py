#entrada
valor = input("Digite o número do seu RM: ")
num = float(valor)

#processamento
u = (num // 1) % 10
d = (num // 10) % 10
c = (num // 100) % 10
m = (num // 1000) % 10
dm = (num // 10000) % 10
soma = u + d + c + m + dm

#saída
print ("A soma dos dígitos do seu RM é: ", soma)