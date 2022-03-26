nome = input("Digite seu nome: ")
valor = input("Digite o seu ano de nascimento: ")
ano = int(valor)
valor2 = input("Digite o seu ano atual: ")
atual = int(valor2)
idade = atual - ano
print(nome, "tem (ou terá)", idade, "anos.")