i = 2
atual = 0
anterior = 0
cont = 0     

n = int(input("Digite o numero de elementos da sequencia: "))
anterior = int(input("Digite o primeiro numero: "))
cont = 1
while i <= n: 
    atual = int(input('Proximo numero: '))
    if atual != anterior:
        cont = cont + 1
        anterior = atual
    i = i + 1

print("Quantidade de segmentos de numeros iguais da sequência = ", cont)

