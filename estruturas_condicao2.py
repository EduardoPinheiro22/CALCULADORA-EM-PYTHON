# Criando a variável tempoExperiencia e atribuindo o valor 5
tempoExperiencia = 5

# Verificando se o tempo de experiência é menor que 2
if tempoExperiencia < 2:
    print('Nível de conhecimento júnior.')
# Verificando se o tempo de experiência é maior que 2 e menor que 5
elif 2 <= tempoExperiencia < 5:
    print('Nível de conhecimento pleno.')
# Se não for nenhum dos casos anteriores, é sênior
else:
    print('Nível de conhecimento sênior.')

# Alterando o valor de tempoExperiencia para 1
tempoExperiencia = 1

# Verificando novamente
if tempoExperiencia < 2:
    print('Nível de conhecimento júnior.')
elif 2 <= tempoExperiencia < 5:
    print('Nível de conhecimento pleno.')
else:
    print('Nível de conhecimento sênior.')

# Alterando o valor de tempoExperiencia para 3
tempoExperiencia = 3

# Verificando novamente
if tempoExperiencia < 2:
    print('Nível de conhecimento júnior.')
elif 2 <= tempoExperiencia < 5:
    print('Nível de conhecimento pleno.')
else:
    print('Nível de conhecimento sênior.')
