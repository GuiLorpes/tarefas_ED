class AlbumFigs:
    ''' 
    Um álbum de figurinhas onde cada figurinha é um inteiro positivo.
    Exemplos
    >>> a = AlbumFigs(300)
    >>> a.show()
    "[]"
    >>> a.add_fig(3)
    >>> a.add_fig(3)
    >>> a.add_fig(1)
    >>> a.add_fig(1)
    >>> a.add_fig(45)
    >>> a.add_fig(400)
    >>> a.show()
    "[1, 3, 45]"
    >>> a.show_rep()
    "[1 (1), 3 (1)]"
    >>> a.rm_fig(1)
    >>> a.rm_fig(45)
    >>> a.rm_fig(500)
    >>> a.show()
    "[1, 3]"
    >>> a.show_rep()
    "[3 (1)]"
    ''' 
    
    # Métodos
    def __init__(self, c: int):
        ''' 
        Cria um novo álbum com *c* figurinhas diferentes.
        '''
        raise NotImplementedError
    
    def add_fig(self, fig:int):
        '''
        Se *fig* estiver no álbum, a quantidade dela é aumentada em 1.
        Caso contrário, *fig* é adicionada ao álbum com quantidade 1.
        Nada acontece se *fig* não estiver no intervalo de figurinhas possíveis do álbum.
        '''
        raise NotImplementedError
    
    def rm_fig(self, fig:int) -> int:
        '''
        Se *fig* estiver no álbum, a quantidade dela é diminuida em 1 e, caso sua quantidade chegue
        a zero, ela é removida do álbum.
        Caso contrário, nada acontece.
        Nada acontece se *fig* não estiver no intervalo de figurinhas possíveis do álbum.
        '''
        raise NotImplementedError
    
    def show(self) -> str:
        '''
        Mostra todos as figurinhas do album sem mostrar as quantias de cada
        '''
        raise NotImplementedError

    def show_rep(self) -> str:
        '''
        Mostra todas as figurinhas repetidas e sua quantidade
        '''
        raise NotImplementedError
    
    def trocas_maximas(self, b: AlbumFigs):
        '''
        Verifica quantas cartas de *self* é possivel trocar com *b*, e troca em
        pares as cartinhas dos dois albuns, caso não seja possivel realizar 
        nenhuma troca, não faz nada.
        Exemplo
        >>> a = AlbumFigs(300)
        >>> a.add_fig(4)
        >>> a.add_fig(4)
        >>> a.add_fig(4)
        >>> a.add_fig(7)
        >>> a.add_fig(7)
        >>> a.add_fig(1)
        >>> a.add_fig(1)
        >>> a.add_fig(1)
        >>> b = AlbumFigs(300)
        >>> b.add_fig(9)
        >>> b.add_fig(9)
        >>> b.add_fig(9)
        >>> b.add_fig(7)
        >>> b.add_fig(7)
        >>> b.add_fig(6)
        >>> b.add_fig(6)
        >>> b.add_fig(10)
        >>> b.add_fig(4)
        >>> b.add_fig(4)
        >>> # Cartinhas antes da troca
        >>> a.show()
        '[1, 4, 7]'
        >>> a.show_rep()
        '[1 (2), 4 (2), 7 (1)]'
        >>> b.show()
        '[4, 6, 7, 9, 10]'
        >>> b.show_rep()
        '[4 (1), 6 (1), 7 (1), 9 (2)]'
        >>> a.trocas_maximas(b)
        >>> # Cartinhas depois das trocas
        >>> a.show()
        '[1, 4, 6, 7]'
        >>> a.show_rep()
        '[1 (1), 4 (2), 7 (1)]'
        >>> b.show()
        '[1, 4, 6, 7, 9, 10]'
        >>> b.show_rep()
        '[4 (1), 7 (1), 9 (2)]'
        >>> # Não tem como trocar mais cartas, não faz nada
        >>> a.trocas_maximas(b)
        >>> a.show()
        '[1, 4, 6, 7]'
        >>> b.show()
        '[1, 4, 6, 7, 9, 10]'
        '''
        raise NotImplementedError
