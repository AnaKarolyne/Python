#input de dados
Frase = input("Digite uma frase qualquer: ")
B = Frase.strip()
contador = 0

#processamento
for letra in B:
    if letra in "aeiouAEIOU":
        contador += 1

#saída
print("A frase digitada têm {} vogais".format(contador))
