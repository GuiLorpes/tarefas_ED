from pilha_modificada import Pilha

def avalia_posfixa(expr: list[str]) -> int:
    '''
    Avalia a expressão posfixa *expr*.

    Requer que cada elemento de *expr* seja uma string que representa um número
    inteiro ou uma das strings '+', '-', '*', '/', que representam a suas
    respectivas operações. *expr* deve representar uma expressão válida.

    Exemplos
    >>> avalia_posfixa(['102'])
    102
    >>> avalia_posfixa(['55', '5', '/'])
    11
    >>> avalia_posfixa(['5', '6', '*', '3', '+'])
    33
    >>> avalia_posfixa(['5', '-6', '*', '3', '+', '10', '-'])
    -37
    '''
    p = Pilha(len(expr))
    for termo in expr:
        if termo in '+-*/':
            b = int(p.desempilha())
            a = int(p.desempilha())
            if termo == '+':
                p.empilha(str(a + b))
            elif termo == '-':
                p.empilha(str(a - b))
            elif termo == '*':
                p.empilha(str(a * b))
            else:
                p.empilha(str(a // b))
        else:
            p.empilha(termo)
    return int(p.desempilha())
