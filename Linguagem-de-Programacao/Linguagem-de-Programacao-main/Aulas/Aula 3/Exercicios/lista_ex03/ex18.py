usuario1 = 'Victor'
senha1 = '2307'

print('-=-' * 10)
print(f'{'CREDÊNCIAIS':^30}')
print('-=-' * 10)

usuario = input('Usuário: ')
senha = input('Senha: ')

if usuario == usuario1 and senha == senha1:
    print('Login bem-sucedido.')
elif usuario != usuario1 or senha != senha1:
    print('Usuário ou senha incorretos.')
    usuario = input('Usuário: ')
    senha = input('Senha: ')

    if usuario == usuario1 and senha == senha1:
        print('Login bem-sucedido.')
    elif usuario != usuario1 or senha != senha1:
        print('Usuário ou senha incorretos.')
        usuario = input('Usuário: ')
        senha = input('Senha: ')

        if usuario == usuario1 and senha == senha1:
            print('Login bem-sucedido.')
        else:
            print('Acesso bloqueado. Número máximo de tentativas atingidas.') 
       
    