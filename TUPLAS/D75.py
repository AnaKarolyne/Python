# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
num = (int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: ')))

print(f'Os numeros digitados foram: {sorted(num)}')

#A) Quantas vezes apareceu o valor 9.
print(f'O número nove (9) apareceu {num.count(9)} vezes dentro dessa tupla.')

#B) Em que posição foi digitado o primeiro valor 3.
print(f'O número três (3) apareceu na posição {num.index(3)} dentro da tupla.')

#C) Quais foram os números pares.
print(f'Os valores pares digitados foram ', end='')
for n in num:
   if n % 2  == 0:
    print(n, end=' ')

#C) Quais foram os números ímpares.
print(f'Os valores ímpares digitados foram ', end='')
for n in num:
   if n % 2  != 0:
    print(n, end=' ')