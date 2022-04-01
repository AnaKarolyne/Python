#Uma equação de 2º grau é da forma: ax2 + bx + c = 0, onde a 6= 0. Escreva um algoritmo que recebe os três coefscientes da equação, calcula e imprime as raízes reais se for possível.
print("Calculadora de equação do 2° grau")
a = float(input("Digite o número que represente o coeficiente A: "))
b = float(input("Digite o número que represente o coeficiente  B: "))
c = float(input("Digite o número que represente o coeficiente  C: "))

#processamento


if (a != 0):
    t = ((b*b) - (4*a*c))
    if (t < 0):
        print("Operação IMPOSSÍVEL de ser realizada! O delta precisa ser maior ou igual ao zero para avançarmos na equação.")

    else:
        import math
        raiz = math.sqrt(t)
        x1 = (-b + raiz)/(2*a)
        x2 = (-b - raiz)/(2*a)
        print(f'Pode se concluir que, as raízes da equação {a:.1f}x² + {b:.1f}x + {c:.1f} = 0 são x1 = {x1:.2f} e x2 = {x2:.2f}.')

else:
    print("Operação IMPOSSÍVEL de ser realizada! A mesma não é uma equação de 2° grau.")