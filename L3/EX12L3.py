print("Cálculo de média ponderada + presença")
m1 = float(input("Digite a média obtida no primeiro semestre: "))
m2 = float(input("Digite a média obtida no segundo semestre: "))
ta = float(input("Digite o total de aulas ministradas no ano: "))
aa = float(input("Digite a quantidade de aulas assistidas: "))

peso = 4 + 6
mp = ((4*m1) + (6*m2))/peso

if (mp < 5) and (aa < (ta*0.7)):
    print("REPROVADO!")

elif (mp < 5) and (aa > (ta*0.7)):
    print("EM EXAME! Estude muito.")

elif (mp == 5) and (aa < (ta*0.7)):
    print("EM EXAME! Dê o seu melhor!")

elif (mp == 5) and (aa > (ta*0.7)):
    print("APROVADO! Passou raspando heim, se esforçe mais da próxima vez.")

elif (mp > 5) and (aa < (ta*0.7)):
    print("EM EXAME! Podê parar de preguiça e começa a frequentar as aulas.")

else:
    print("APROVADO! Meus parabéns, você é o novo queridinho do professor!")

