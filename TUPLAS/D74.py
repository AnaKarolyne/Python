#Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
from random import randint
from tkinter.tix import MAX
n = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))

print(f'Eu sortiei os valores {n}')
print(f'Em ordem ficaria {sorted(n)}')
print(f'O MENOR valor é: {min(n)}')
print(f'O MAIOR valor é: {max(n)}')