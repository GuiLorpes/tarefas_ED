from lista_modificada import Lista


def primos(lim: int) -> Lista:
    '''
    Encontra todos os números primos menores que *lim*.

    Exemplos:
    >>> primos(2).str()
    '[]'
    >>> primos(20).str()
    '[2, 3, 5, 7, 11, 13, 17, 19]'
    '''
    primos = Lista()
    n = 2
    while n < lim:
        eh_primo = True
        i = 0
        while eh_primo and i < primos.num_itens():
            if n % primos.get(i) == 0:
                eh_primo = False
            i = i + 1

        if eh_primo:
            primos.insere(primos.num_itens(), n)

        n = n + 1
    return primos
