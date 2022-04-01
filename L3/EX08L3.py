#Escreva um algoritmo que recebe a idade de um nadador e mostra sua categoria.
i=int(input("Digite a idade do nadador: "))

if (i >= 5) and (i <= 7):
    print ("O nadador pertence a categoria: INFANTIL.")
    if (i < 5): 
        print ("Não existe uma categoria para essa idade.")

elif (i <= 10):
    print ("O nadador pertence a categoria: JUVENIL.")

elif (i <= 15):
    print ("O nadador pertence a categoria: ADOLESCENTE.")

elif (i <= 30):
    print ("O nadador pertence a categoria: ADULTO.")

else:
    print ("O nadador pertence a categoria: SENIOR.")        
