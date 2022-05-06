#Faça um algoritmo que receba um número que é a quantidade da sequência que você irá escrever:
num = float(input("Digite um número qualquer: "))

#Escreva a sua sequência:
while True:
    try:
        texto = input('Digite uma sequência de números com a quantidade exata que você digitou acima: ')
        if texto.isnumeric() and len(texto) == num: # é um "número" de 3 dígitos
            break # sai do loop
        print('A sequência deve ter exatamente a quantidade que você digitou.')
    except ValueError:
        print('Não foi digitado o que foi pedido.')



