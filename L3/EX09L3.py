#No exercício da calculadora, visto em sala de aula, temos um problema com a operação de divisão. Sua tarefa será exibir uma mensagem informando que é impossível fazer uma divisão por 0. Note que, essa mensagem só deverá aparecer quando o usuário quiser fazer tal operação
num = int(input("Digite o primeiro número: "))
num1 = int(input("Digite o segundo número: "))

if (num1 != 0):
    print(f'O valor da divisão de {num:.0f} por {num:.0f} é igual a {num/num1:.1f}.')

else:
    print("Operação IMPOSSÍVEL de ser realizada!")    