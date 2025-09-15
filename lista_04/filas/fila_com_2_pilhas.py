from pilha_arranjo import Pilha
class Fila:
    '''
    Uma coleção de strings que segue a política FIFO: o primeiro a ser inserido
    é o primeiro a ser removido.

    Exemplos
    >>> f = Fila(60)
    >>> f.vazia()
    True
    >>> f.enfileira('Amanda')
    >>> f.enfileira('Fernando')
    >>> f.enfileira('Márcia')
    >>> f.vazia()
    False
    >>> f.desenfileira()
    'Amanda'
    >>> f.enfileira('Pedro')
    >>> f.enfileira('Alberto')
    >>> while not f.vazia():
    ...     f.desenfileira()
    'Fernando'
    'Márcia'
    'Pedro'
    'Alberto'
    '''
    pilha1: Pilha
    pilha2: Pilha
    capa: int

    def __init__(self, c: int):
        self.pilha1 = Pilha(c)
        self.pilha2 = Pilha(c)
        self.capa = c

    def enfileira(self, item: str):
        '''
        Adiciona *item* no final da fila.
        >>> f = Fila(60)
        >>> f.vazia()
        True
        >>> f.enfileira('a')
        >>> f.enfileira('b')
        >>> f.enfileira('c')
        >>> f.desenfileira()
        'a'
        '''
        if self.pilha1.vazia() and self.pilha2.vazia():
            self.pilha1.empilha(item)
        else:
            while not self.pilha2.vazia():
                p = self.pilha2.desempilha()
                self.pilha1.empilha(p)
            self.pilha1.empilha(item)

    def desenfileira(self) -> str:
        '''
        Remove e devolve o primeiro elemento da fila.

        Requer que a fila não esteja vazia.
        '''
        if self.pilha1.vazia() and self.pilha2.vazia():
            raise ValueError ('Fila vazia')
        else:
            while not self.pilha1.vazia():
                p = self.pilha1.desempilha()
                self.pilha2.empilha(p)
        return self.pilha2.desempilha()

    def vazia(self) -> bool:
        '''
        Devolve True se a fila está vazia, False caso contrário.
        '''
        return self.pilha1.vazia() and self.pilha2.vazia()
