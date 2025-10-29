class FilaDupla:
    '''
    Uma coleção de strings que segue a política de fila dupla, ou seja, os
    elementos podem ser inseridos e removidos de qualquer extremo (aqui
    chamados de início e fim).

    Exemplos
    >>> f = FilaDupla()
    >>> f.vazia()
    True
    >>> f.insere_esquerda('casa')
    >>> f.insere_esquerda('minha')
    >>> f.insere_direita('é')
    >>> f.insere_direita('verde')
    >>> f.insere_direita('legal')
    >>> f.insere_direita('né?')
    >>> f.vazia()
    False
    >>> f.remove_esquerda()
    'minha'
    >>> f.remove_esquerda()
    'casa'
    >>> f.remove_esquerda()
    'é'
    >>> f.remove_esquerda()
    'verde'
    >>> f.remove_direita()
    'né?'
    >>> f.remove_direita()
    'legal'
    >>> f.remove_esquerda()
    Traceback (most recent call last):
    ...
    ValueError: fila vazia
    >>> f.remove_direita()
    Traceback (most recent call last):
    ...
    ValueError: fila vazia
    '''

    def insere_esquerda(self, item: str):
        '''
        Insere *item* no início da fila.
        '''
        raise NotImplementedError

    def remove_esquerda(self) -> str:
        '''
        Remove e devolve o item no início da fila.

        Requer que a fila não esteja vazia.
        '''
        raise NotImplementedError

    def insere_direita(self, item: str):
        '''
        Insere *item* no fim da fila.
        '''
        raise NotImplementedError

    def remove_direita(self) -> str:
        '''
        Remove e devolve o item no fim da fila.

        Requer que a fila não esteja vazia.
        '''
        raise NotImplementedError

    def vazia(self) -> bool:
        '''
        Devolve True e a fila está vazia, False caso contrário.
        '''
        raise NotImplementedError
