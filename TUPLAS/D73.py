#Crie uma tupla preenchida com os 12 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
Pessoas = ('Karol', 'Sérgio', 'Antonio', 'Gustavo', 'Iago', 'Valentina', 
        'Alan', 'João', 'Matheus', 'Leo', 'Cida', 'Dora')
#a) Os 5 primeiros times.
print(f'Os 5 primeros são: {Pessoas[:5]}')

#b) Os últimos 4 colocados.
print(f'Os últimos 4 colocados são: {Pessoas[-4:]}')

#c) Times em ordem alfabética.
print(f'Em ordem alfabética: {sorted(Pessoas)}')

#d) Em que posição está o time da Chapecoense.
print(f'Matheus está na posição {Pessoas.index("Matheus")}')