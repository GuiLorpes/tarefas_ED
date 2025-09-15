from fila_arranjo_circular import Fila

class Pilha:
    '''
    Uma coleção de strings que segue a política LIFO: o elemento mais
    recentemente inserido é o primeiro a ser removido.

    >>> p = Pilha(60)
    >>> p.vazia()
    True
    >>> p.empilha('O')
    >>> p.empilha('que')
    >>> p.empilha('escrever?')
    >>> p.vazia()
    False
    >>> p.desempilha()
    'escrever?'
    >>> p.empilha('fazer')
    >>> p.empilha('agora?')
    >>> while not p.vazia():
    ...     p.desempilha()
    'agora?'
    'fazer'
    'que'
    'O'
    '''
    fila1: Fila
    fila2: Fila
    capa: int
    itens: int

    def __init__(self, c: int):
        self.fila1 = Fila(c)
        self.fila2 = Fila(c)
        self.capa = c
        self.itens = 0

    def empilha(self, item: str):
        '''
        Adiciona o *item* na pilha.
        '''
        if self.vazia():
            self.fila1.enfileira(item)
        else:
            if self.fila1.vazia():
                self.fila2.enfileira(item)
            else: # self.fila2.vazia()
                self.fila1.enfileira(item)
        self.itens += 1

    def desempilha(self) -> str:
        '''
        Devolve o elemento mais recentemente adicionado da pilha.

        Requer que a pilha não esteja vazia.
        '''
        if self.vazia():
            raise ValueError ('Pilha vazia!')
        else:
            if self.fila2.vazia():
                for i in range (self.itens - 1):
                    f = self.fila1.desenfileira()
                    self.fila2.enfileira(f)
                r = self.fila1.desenfileira()
            else: # self.fila1.vazia()
                for i in range (self.itens - 1):
                    f = self.fila2.desenfileira()
                    self.fila1.enfileira(f)
                r = self.fila2.desenfileira()
            self.itens -= 1
        return r

    def vazia(self) -> bool:
        '''
        Devolve True se a pilha está vazia, False caso contrário.

        Exemplos
        >>> p = Pilha(60)
        >>> p.vazia()
        True
        >>> p.empilha('lar')
        >>> p.vazia()
        False
        '''
        return self.fila1.vazia() and self.fila2.vazia()