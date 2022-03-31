#Escreva um algoritmo que calcule o que deve ser pago por um produto, considerando o preço normal de etiqueta e a escolha da condição de pagamento. Utilize os códigos da tabela a seguir para ler qual a condição de pagamento escolhida e efetuar o cálculo adequado.
print("Cálculo do valor pago com base na forma de pagamento.")
v = float(input("Digite o valor da mercadoria em reais: "))
c = float(input("Forma de pagamento desejada: "))

if (c == 1):
    vista = v * 0.9
    print(f'O valor do produto com desconto de 10% será de R$ {vista:.2f}')

elif (c == 2):
    credito = v * 0.05
    print(f'O valor do produto com desconto de 5% será de R$ {credito:.2f}')

elif (c == 3):
    print(f'O valor do produto será de R${v:.2f}')

else:
    juros = (v * 0.07)
    soma = v + juros
    print(f'O valor do produto com juros de 7% será de R$ {soma:.2f}')

