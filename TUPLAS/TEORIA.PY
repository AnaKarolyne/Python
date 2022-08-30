#------------------------     TUPLAS      ------------------------#

#Tuplas são váriaveis compostas e IMUTÁVEIS que permitem armazenar vários valores em uma única estrutura acessado por chaves individuais.
#Aceita diferentes tipos de elementos dentro dela.

#Váriavel Simples
#lanche = 'suco'
#lanche = 'hamburguer'
                            #Um valor substitui o outro, assim vc só pode ter o 'suco' ou o 'hamburguer' de cada vez.

#Váriavel Composta
lanche = 'suco', 'hamburguer', 'pudim', 'batata'
#           0         1           2       3                   
                             #Um valor NÃO substitui o outro, assim vc pode escolher um combo com 'suco', 'hamburguer', 'pudim' e 'batata'.
#Nessa váriavel composta, os elementos são indentificados por um índice. 
# Exemplo:
#lanche[0]= 'suco'  lanche[1]= 'hamburguer'...  lanche [0,2]='suco', 'hamburguer'   lanche[1:]='hamburguer', 'pudim', 'batata'  lanche[-4]= 'suco'

print(len(lanche)) #Printa a quantidade de elementos na variavel 'lanche'

for c in lanche:
    print(c) #Um loop que lê cada elemento 'c' dentro de lanche

                            
                            
