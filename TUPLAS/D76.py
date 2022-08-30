#Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.
Lista = ('Lápis', 1.75, 'Caderno', 9.99, 'Borracha', 2, 'Canetas', 5.50, 'Régua', 3.81)

print('-' * 35)
print('LISTAGEM DE PREÇOS')
print('-' * 35)

for pos in range(0, len(Lista)):
    if pos % 2 == 0:
        print(f'{Lista[pos]:.<30}', end='')
    else:
        print(f'R${Lista[pos]:>5.2f}')