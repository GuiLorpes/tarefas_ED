from ed import array

class Pilha:
    '''
    Uma coleção de strings que segue a política LIFO: o elemento mais
    recentemente inserido é o primeiro a ser removido.

    >>> p = Pilha(80)
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

    valores: array[str]
    # O índice do elemento que está no topo da pilha,
    # -1 se a pilha está vazia.
    topo: int
    capacidade: int

    def __init__(self, c: int) -> None:
        '''
        Cria uma nova pilha com capacidade para armazenar *CAPACIDADE*
        elementos.
        '''
        self.valores = array(c, '')
        self.topo = -1
        self.capacidade = c

    def empilha(self, item: str):
        '''
        Adiciona o *item* na pilha.

        Requer que a quantidade de elementos na pilha seja menor que
        *CAPACIDADE*.

        Exemplos
        >>> p = Pilha(80)
        >>> for i in range(p.capacidade):
        ...     p.empilha(str(i))
        >>> p.empilha('a')
        Traceback (most recent call last):
        ...
        ValueError: pilha cheia
        >>> p.cheia()
        True
        >>> p.desempilha() == str(p.capacidade - 1)
        True
        '''
        if self.cheia():
            raise ValueError('pilha cheia')
        self.topo += 1
        self.valores[self.topo] = item

    def desempilha(self) -> str:
        '''
        Devolve o elemento mais recentemente adicionado da pilha.

        Requer que a pilha não esteja vazia.

        Exemplos
        >>> p = Pilha(80)
        >>> p.desempilha()
        Traceback (most recent call last):
        ...
        ValueError: pilha vazia
        >>> p.empilha('casa')
        >>> p.empilha('na')
        >>> p.empilha('árvore')
        >>> p.desempilha()
        'árvore'
        '''
        if self.vazia():
            raise ValueError('pilha vazia')
        item = self.valores[self.topo]
        self.topo -= 1
        return item

    def vazia(self) -> bool:
        '''
        Devolve True se a pilha está vazia, False caso contrário.

        Exemplos
        >>> p = Pilha(80)
        >>> p.vazia()
        True
        >>> p.empilha('lar')
        >>> p.vazia()
        False
        '''
        return self.topo == -1

    def cheia(self) -> bool:
        ''' 
        Devolve True se a pilha estiver cheia, False caso contrario.
        Exemplo
        >>> p = Pilha(2)
        >>> p.empilha('a')
        >>> p.cheia()
        False
        >>> p.empilha('b')
        >>> p.cheia()
        True
        '''
        return self.topo == self.capacidade - 1
    
    def esvazia(self):
        '''
        Esvazia a pilha
        Exemplos
        >>> p = Pilha(10)
        >>> p.vazia()
        True
        >>> p.empilha('a')
        >>> p.empilha('a')
        >>> p.vazia()
        False
        >>> p.esvazia()
        >>> p.vazia()
        True
        '''
        self.topo = -1