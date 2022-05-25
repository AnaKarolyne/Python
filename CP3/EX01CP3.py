#Criar lista:
LP = []
Produto = input("Insira um Produto: ")
LP.append(Produto)

LQ = []
Quantidade = input("Insira a quantidade: ")
Q1 = int(Quantidade)
LQ.append(Q1)

LPr = []
Preco = input("Insira o preço: ")
P1 = float(Preco)
LPr.append(P1)

while Quantidade < 0:
    NProduto = input("Insira um Produto: ")
    LP.append(NProduto)

    NQuantidade = input("Insira a quantidade: ")
    N1 = int(NQuantidade)
    LQ.append(N1)

    NPreco = input("Insira o preço: ")
    NP1 = int(NPreco)
    LPr.append(NP1)

print(LP)
print(LQ)
print(LPr)

