def main(a: float, b: float, c: float) -> str:
    '''retorna o tipo de um triângulo com base nos valores de seus lados.
    >>> main(3, 3, 3)
    'triângulo equilátero'

    >>> main(3, 3, 5)
    'triângulo isósceles'

    >>> main(3, 4, 5)
    'triângulo escaleno'
    
    >>> main(3, 3, 7)
    'não é triângulo'
    '''
    if a == b and b == c:
        return 'triângulo equilátero'
    elif (a == b or b == c or c == a) and c < a + b:
        return 'triângulo isósceles'
    elif a < b + c and c < a + b and b < a + c:
        return 'triângulo escaleno'
    else:
        return 'não é triângulo'