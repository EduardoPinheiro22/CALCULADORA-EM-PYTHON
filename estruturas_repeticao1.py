# Criando a variável entrada_idade e atribuindo a ela o valor ''
entrada_idade = ''

# Instrução while para continuar pedindo entradas até o valor ser 0
while str(entrada_idade) != '0':
    # Atribuindo à variável entrada_idade o valor digitado pelo usuário
    entrada_idade = input('Digite um número qualquer ou 0 para sair: ')
    
    # Imprimindo o número digitado
    print('Número digitado:', entrada_idade)
