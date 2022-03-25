valor = input("Digite um valor entre 0 a 999: ")
num = float(valor)
unidade = num % 10
dezena = (num // 10) % 10
num2 = (num  - unidade) / 10
centena = (num2 - dezena) / 10
print ("O valor da sua centena é:", centena)
print ("O valor da sua dezena é:", dezena)
print ("O valor da sua unidade é:", unidade)