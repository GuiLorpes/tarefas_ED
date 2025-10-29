from pilha_modificada import Pilha


def inverte_pilha(p: Pilha):
    '''
    Inverte a ordem dos elemento de *p*.

    Exemplos
    >>> p = Pilha(10)
    >>> p.empilha('um')
    >>> p.empilha('carro')
    >>> p.empilha('mouse')
    >>> inverte_pilha(p)
    >>> p.desempilha()
    'um'
    >>> p.desempilha()
    'carro'
    >>> p.desempilha()
    'mouse'
    '''
    a = Pilha(p.capacidade())
    b = Pilha(p.capacidade())
    move_todos(p, a)
    move_todos(a, b)
    move_todos(b, p)


def remove_vazios(p: Pilha):
    '''
    Temove todos os elementos vazios de *p*.

    Exemplos
    >>> p = Pilha(10)
    >>> p.empilha('um')
    >>> p.empilha('')
    >>> p.empilha('carro')
    >>> p.empilha('')
    >>> p.empilha('')
    >>> remove_vazios(p)
    >>> p.desempilha()
    'carro'
    >>> p.desempilha()
    'um'
    '''
    a = Pilha(p.capacidade())
    while not p.vazia():
        item = p.desempilha()
        if item != '':
            a.empilha(item)
    move_todos(a, p)


def move_todos(a: Pilha, b: Pilha):
    '''
    Desempilha todos os elementos de *a* e empilha em *b*.

    Exemplos
    >>> a = Pilha(10)
    >>> a.empilha('a')
    >>> a.empilha('b')
    >>> a.empilha('c')
    >>> b = Pilha(10)
    >>> move_todos(a, b)
    >>> a.vazia()
    True
    >>> b.desempilha()
    'a'
    >>> b.desempilha()
    'b'
    >>> b.desempilha()
    'c'
    >>> b.vazia()
    True
    '''
    while not a.vazia():
        b.empilha(a.desempilha())
