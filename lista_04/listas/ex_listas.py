from lista_arranjo import Lista

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
        while eh_primo and i < primos.tamanho:
            if n % primos.get(i) == 0:
                eh_primo = False
            i = i + 1

        if eh_primo:
            primos.acrescenta(n)

        n = n + 1
    return primos

def remove_rep_consec(lst: Lista):
    '''
    Remove os itens repetidos consecutivis de *lst*, deixando somente sua 
    primeira ocorrencia
    Exemplos:
    >>> a = Lista()
    >>> a.acrescenta(1)
    >>> a.acrescenta(1)
    >>> a.acrescenta(2)
    >>> a.acrescenta(2)
    >>> a.acrescenta(2)
    >>> a.acrescenta(1)
    >>> a.acrescenta(6)
    >>> a.acrescenta(6)
    >>> a.acrescenta(6)
    >>> a.str()
    '[1, 1, 2, 2, 2, 1, 6, 6, 6]'
    >>> remove_rep_consec(a)
    >>> a.str()
    '[1, 2, 1, 6]'
    '''
    i = 0
    while i < lst.tamanho:
        while i + 1 != lst.tamanho and lst.get(i) == lst.get(i+1):
            lst.remove(i+1)
        i += 1
        