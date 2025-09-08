def parenteses_corretos(expr: str) -> bool:
    '''
    Produz True se os parênteses de *expr*
    estão corretos.

    Exemplos:
    >>> parenteses_corretos('()')
    True
    >>> parenteses_corretos('(')
    False
    >>> parenteses_corretos(')')
    False
    >>> parenteses_corretos('())')
    False
    >>> parenteses_corretos('((a)*(b-c)-10)*((4-2)/8)')
    True
    '''
    abertos = 0
    corretos = True
    i = 0
    while i < len(expr) and corretos:
        if expr[i] == '(':
            abertos = abertos + 1
        elif expr[i] == ')':
            abertos = abertos - 1
            if abertos < 0:
                corretos = False
        i = i + 1
    return abertos == 0 and corretos
