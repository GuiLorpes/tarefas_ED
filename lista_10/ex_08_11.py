from __future__ import annotations
from dataclasses import dataclass

@dataclass
class Removido:
    pass

@dataclass
class Presente:
    chave: str
    valor: int

class Dicionario:
    '''
    Exemplo
    >>> d = Dicionario(7)
    >>> d.associa('pinto', 69)
    >>> d.associa('sexo', 420)
    >>> d.busca('bct')
    >>> d.busca('pinto')
    69
    >>> d.busca('sexo')
    420
    >>> d.associa('pinto', 19)
    >>> d.associa('bct', 69)
    >>> d.busca('pinto')
    19
    >>> d.busca('bct')
    69
    >>> d.remove('sexo')
    420
    >>> d.busca('sexo')
    '''
    tabela: list[None | Removido | Presente]
    num_itens: int
    num_removidos: int

    def __init__(self, m: int):
        self.tabela = [None] * m
        self.num_itens = 0
        self.num_removidos = 0
    
    def busca(self, chave: str) -> int | None:
        ''' 
        Procura pelo valor da *chave* em *self* e o retorna, se *chave* não
        estiver em *self*, retornar nada
        '''
        p = hash(chave) % len(self.tabela)
        t = self.tabela[p]
        while t is not None:
            if isinstance(t, Presente):
                if t.chave == chave:
                    return t.valor
            p = (p + 1) % len(self.tabela)
            t = self.tabela[p]
        return None
    
    def associa(self, chave: str, valor: int):
        p = hash(chave) % len(self.tabela)
        t = self.tabela[p]
        while t is not None:
            if isinstance(t, Presente):
                if t.chave == chave:
                    t.valor = valor
                    return None
            p = (p + 1) % len(self.tabela)
            t = self.tabela[p]
        self.tabela[p] = Presente(chave, valor)
        self.num_itens += 1

    def remove(self, chave: str) -> int | None:
        if self.num_itens == 0:
            raise ValueError('Não é possivel remover de um dicionário vazio')
        p = hash(chave) % len(self.tabela)
        t = self.tabela[p]
        while t is not None:
            if isinstance(t, Presente):
                if t.chave == chave:
                    i = t.valor
                    self.tabela[p] = Removido()
                    self.num_itens -= 1            
                    self.num_removidos += 1
                    return i
            p = (p + 1) % len(self.tabela)
            t = self.tabela[p]
        return None
        
    def mapeia(self, chave: str) -> int:
        '''
        Exemplos
        >>> d = Dicionario(9)
        >>> for i in [5, 28, 19, 15, 20, 33, 12, 17]:
        ...     associa(str(i), i)
        >>> for i in [5, 28, 19, 15, 20, 33, 12, 17]:
        ...     print
        '''
        A = 1.618033
        return int(len(self.tabela) * ((hash(chave) * A) % 1))