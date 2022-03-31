#A jornada de trabalho diária de um trabalhador é de 8 horas. Caso o trabalhador tenha trabalhado além da jornada mensal exigida, ele terá direito a receber hora-extra. O valor da hora-extra é o valor que ele recebe por hora acrescido de 50%.
qDiasTrabalhadas = float(input("Digite o total de dias úteis no mês: "))
qHorasTrabalhadas = float(input("Digite o total de horas trabalhadas: "))
vHorasTrabalhadas = float(input("Digite o valor da sua hora: "))

JornadaTrabalho = 8
qHorasTrabalhadas = qDiasTrabalhadas * JornadaTrabalho
qtHorasExtras = qHorasTrabalhadas - qHorasTrabalhadas
valorHorasExtras = vHorasTrabalhadas + (vHorasTrabalhadas*(50/100))
salario = (qDiasTrabalhadas * qHorasTrabalhadas) * vHorasTrabalhadas

if (qHorasTrabalhadas < qHorasTrabalhadas):
    print (f'Sálario sem horas extras é de R${salario:.2f}')

else:
    print ("Sálario com horas extras é de R${:.2f}".formart((qtHorasExtras * valorHorasExtras) + salario))