#Faça um programa para ler dois números inteiros A e B e informar se A é divisível por B.
valor = int(input("Digite o primeiro número: "))
valor2 = int(input("Digite o segundo número: "))

divisao = valor % valor2

print ("O resto da divisão é: ", divisao)

if (divisao == 0):
    print("O primeiro número é DIVISÍVEL pelo segundo.")

else:
    print("O primeiro número é NÃO DIVISÍVEL pelo segundo.")
