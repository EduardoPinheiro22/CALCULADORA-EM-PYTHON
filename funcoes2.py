# Definindo a função loginUsuario que recebe o parâmetro perfil
def loginUsuario(perfil):
    # Verificando se o valor do parâmetro perfil é igual a 'admin' (ignorando maiúsculas/minúsculas)
    if perfil.lower() == 'admin':
        print('Bem-vindo, Administrador')
    else:
        print('Bem-vindo, Usuário')

# Chamando a função com diferentes valores como parâmetro

# Testando com 'Admin'
loginUsuario('Admin')

# Testando com 'admin'
loginUsuario('admin')

# Testando com 'User'
loginUsuario('User')

# Testando com 'usuário'
loginUsuario('usuário')

# Testando com 'ADMIN' (variação maiúscula)
loginUsuario('ADMIN')

# Testando com 'usuario' (para um usuário normal)
loginUsuario('usuario')

# Testando com um novo valor para garantir mais variações (exemplo: 'guest')
loginUsuario('guest')

# Testando com outro tipo de entrada (exemplo: 'moderator')
loginUsuario('moderator')
