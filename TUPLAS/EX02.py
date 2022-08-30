a = (1, 3, 4, 8, 9)
b = (8, 9, 2, 4, 4)
c = b + a
d = a + b
print(c.count(4)) #Conta a quantidade de vezes que o elemento entre () apareceu na tupla.
print(c)
print(d)
print(c.index(9, 1)) #Ele mostra em que posição está o elemento entre (), o 9, dentro da tupla apartir da posição 1
del(d) #Apesar de ser imutável, podemos apagar uma tupla INTEIRA com o comando DEL, mas não um elemento em específico.