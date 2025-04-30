def main(password: str) -> bool:
    '''Verifica se a senha digitada no input da função é a senha correta.
    >>> main('senha')
    True

    >>> main('Senha')
    False

    >>> main('senha123')
    False

    >>> main('akjfhdjskl')
    False
    '''
    return password == 'senha' 