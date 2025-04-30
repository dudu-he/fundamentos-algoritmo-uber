def main(comprimento: float, altura: float) -> int:
    '''Calcula a quantidade de azulejos inteiros necessários
    para preencher uma parede com azulejos.
    >>> main(5, 3)
    375
    >>> main(5.1, 3.5)
    447
    '''
    if (comprimento * altura / 0.04) % 1 == 0:
        return int(comprimento * altura / 0.04)
    else:
        return int((comprimento * altura / 0.04) + 1)