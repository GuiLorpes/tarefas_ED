import ed
from fila_arranjo_circular import Fila
from pilha_arranjo import Pilha

def inverte_fila(fila: Fila):
    '''
    Inverte uma fila
    >>> f = Fila(90)
    >>> f.enfileira('a')
    >>> f.enfileira('b')
    >>> f.enfileira('c')
    >>> inverte_fila(f)
    >>> f.desenfileira()
    'c'
    '''
    pilha_aux = Pilha(fila.capacidade())
    while not fila.vazia():
        f = fila.desenfileira()
        pilha_aux.empilha(f)
    while not pilha_aux.vazia():
        p = pilha_aux.desempilha()
        fila.enfileira(p)

