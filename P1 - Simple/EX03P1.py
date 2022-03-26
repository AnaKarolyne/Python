#Faça um programa em Python que leia um valor inteiro e mostre a tabuada de 1 a 10 do valor lido.
print ("TABUADA MÁGICA")
num = input("Escolha um número para descobrir a tabuada: ")
t = int(num)

print('\n Tabuada de', t, ':')

for i in range (1, 11):
    print(num, 'X', i, '=', (t * i))