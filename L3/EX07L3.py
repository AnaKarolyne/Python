#Escreva um algoritmo que lê um número qualquer e retorna a raiz quadrada desse número se possível.
import math
num = float(input("Digite um número qualquer: "))
raiz = math.sqrt(num)
print(f'A raiz quadrada de {num:.1f} é {raiz:.1f}')