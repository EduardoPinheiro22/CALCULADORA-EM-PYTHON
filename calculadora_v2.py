# Função para somar dois números
def adicao(num1, num2):
    return num1 + num2

# Função para subtrair dois números
def subtracao(num1, num2):
    return num1 - num2

# Função para multiplicar dois números
def multiplicacao(num1, num2):
    return num1 * num2

# Função para dividir dois números
def divisao(num1, num2):
    if num2 == 0:
        return "Não foi possível realizar a divisão por 0"
    else:
        return num1 / num2

# Função calculadora que recebe dois números e uma operação
def calculadora(num1, num2, operacao):
    if operacao == "+" or operacao.lower() == "adicao":
        resultado = adicao(num1, num2)
    elif operacao == "-" or operacao.lower() == "subtracao":
        resultado = subtracao(num1, num2)
    elif operacao == "*" or operacao.lower() == "multiplicacao":
        resultado = multiplicacao(num1, num2)
    elif operacao == "/" or operacao.lower() == "divisao":
        resultado = divisao(num1, num2)
    else:
        return "Operação inválida"
    return resultado

# Variável de controle para o laço while
saida = ''

# Laço while para continuar executando o programa até que o usuário escolha sair
while saida != 'n' and saida != 'N':
    # Solicitando os números e a operação
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        operacao = input("Digite a operação (+, -, *, / ou o nome da operação como adicao, subtracao, multiplicacao, divisao): ")
    except ValueError:
        print("Por favor, insira valores numéricos válidos.")
        continue
    
    # Chamando a função calculadora
    resultado = calculadora(num1, num2, operacao)
    
    # Exibindo o resultado da operação
    print(f"Resultado da operação: {resultado}")
    
    # Perguntando ao usuário se deseja continuar ou sair
    saida = input("Deseja realizar outra operação? (S/N): ")

# Finalizando o programa
print("Obrigado por usar a calculadora!")

# f