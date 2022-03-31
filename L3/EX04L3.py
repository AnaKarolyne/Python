#Escreva um algoritmo para ler o nome de 2 times e o número de gols marcados em uma partida. Escrever o nome do vencedor. Caso não haja vencedor deverá ser impresso a palavra EMPATE.
t1 = input("Digite o nome do time da casa: ")
g1 = int(input("Digite a quantidade de gols marcados pelo time da casa: "))

t2 = input("Digite o nome do time rival: ")
g2 = int(input("Digite a quantidade de gols marcados pelo time rival: "))

if (g1 == g2):
    print("EMPATE!")

elif (g1 > g2):
    print(t1, "é o time VENCEDOR!", t2, "vai voltar para casa chupando dedo.")

else:
    print(t2, "é o time VENCEDOR!", t1, "é um bebê chorão!")