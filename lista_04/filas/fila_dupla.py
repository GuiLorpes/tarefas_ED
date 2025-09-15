from ed import array

class FilaDupla:
    '''
    Uma fila dupla onde pode se colocar e excluir itens pela direita e esquerda
    Exemplo
    >>> d = FilaDupla(80)
    >>> d.vazia()
    True
    >>> d.appendRight('a')
    >>> d.appendLeft('b')
    >>> d.appendLeft('a')
    >>> d.vazia()
    False
    >>> d.popRight()
    'a'
    >>> d.popLeft()
    'a'
    >>> d.popRight()
    'b'
    '''
    itens: array[str]
    inicio: int
    fim: int
    capacidade: int

    def __init__(self, c: int):
        ''' Cria uma nova fila dupla com capacidade *c*'''
        self.itens = array(c + 1, '')
        self.inicio = 0
        self.fim = 0
        self.capacidade = c

    def appendRight(self, item: str):
        ''' Adiciona um *item* no fim da fila '''
        raise NotImplementedError
    
    def appendLeft(self, item: str):
        ''' Adiciona um *item* no começo da fila '''
        raise NotImplementedError
    
    def popRight(self) -> str:
        ''' Remove o ultimo item da fila '''
        raise NotImplementedError

    def popLeft(self) -> str:
        ''' Remove o primeiro item da fila '''
        raise NotImplementedError