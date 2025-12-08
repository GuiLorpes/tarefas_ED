from __future__ import annotations

class Conjunto:
    '''
    Um conjunto de números inteiros
    Exemplos
    >>> c1 = Conjunto()
    >>> c1.adiciona(2)
    >>> c1.adiciona(3)
    >>> c1.adiciona(4)
    >>> c1.mostra()
    '{2, 3, 4}'
    >>> c2 = Conjunto()
    >>> c2.adiciona(1)
    >>> c2.adiciona(2)
    >>> c2.adiciona(4)
    >>> c2.mostra()
    '{1, 2, 4}'
    >>> c3 = c1.uniao(c2)
    >>> c3.mostra()
    '{1, 2, 3, 4}'
    '''
    
    def __init__(self) -> None:
        '''Cria um novo conjunto vazio.'''
        raise NotImplementedError
    
    def adiciona(self, n: int) -> None:
        '''Adiciona *n* ao conjunto.'''
        raise NotImplementedError
    
    def mostra(self) -> str:
        '''Cria uma string com os elementos entre chaves e separados por vírgula.'''
        raise NotImplementedError
    
    def uniao(self, outro: Conjunto) -> Conjunto:
        '''Realiza a união entre *self* e *outro*.'''
        raise NotImplementedError