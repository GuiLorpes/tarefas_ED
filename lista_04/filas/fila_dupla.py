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
    tamanho: int

    def __init__(self, c: int):
        ''' Cria uma nova fila dupla com capacidade *c*'''
        self.itens = array(c + 1, '')
        self.inicio = 0
        self.fim = 0
        self.capacidade = c
        self.tamanho = 0

    def appendRight(self, item: str):
        ''' 
        Adiciona um *item* no fim da fila 
        Exemplos
        >>> f = FilaDupla(60)
        >>> f.appendRight('a')
        >>> f.appendRight('b')
        >>> f.popRight()
        'a'
        '''
        if self.cheia():
            raise ValueError('Fila cheia!')
        self.itens[self.fim] = item
        self.tamanho += 1
        if self.fim == self.capacidade:
            self.fim = 0
        else:
            self.fim += 1
    
    def appendLeft(self, item: str):
        ''' Adiciona um *item* no começo da fila '''
        if self.cheia():
            raise ValueError('Fila cheia!')
        if self.inicio == 0:
            self.itens[self.capacidade] = item
            self.inicio = self.capacidade
        else:
            self.itens[self.inicio] = item
        self.tamanho += 1
        self.inicio -= 1

    def popRight(self) -> str:
        ''' Remove o ultimo item da fila '''
        if self.vazia():
            raise ValueError('Fila vazia!')
        item = self.itens[self.fim]
        if self.fim == 0:
            self.fim = self.capacidade
        else:
            self.fim -= 1
        self.tamanho -= 1
        return item

    def popLeft(self) -> str:
        ''' Remove o primeiro item da fila '''
        raise NotImplementedError
        self.tamanho -= 1
        self.inicio += 1

    def vazia(self) -> bool:
        ''' Verifica se a fila dupla está vazia '''
        return self.fim == self.inicio
    
    def cheia(self) -> bool:
        ''' Verifica se a fila dupla está cheia '''
        return self.fim + 1 == self.inicio or \
            self.fim == self.capacidade and self.inicio == 0    
    def len(self) -> int:
        ''' Retorna a quantia de itens da fila '''
        return self.tamanho
    
    def esvazia(self):
        ''' Esvazia uma fila dupla '''
        self.fim = self.inicio
    
