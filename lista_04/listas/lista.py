from __future__ import annotations
from ed import array

CAPACIDADE_INICIAL: int = 4
FATOR_CRESCIMENTO: float = 2.0

class Lista:
    '''
    Uma sequência de números.

    Exemplos
    >>> lst = Lista()
    >>> lst.str()
    '[]'
    >>> lst.insere(0, 7)
    >>> lst.insere(1, 20)
    >>> lst.insere(2, 5)
    >>> lst.get(0)
    7
    >>> lst.get(2)
    5
    >>> lst.num_itens()
    3
    >>> lst.str()
    '[7, 20, 5]'
    >>> lst.set(0, 10)
    >>> lst.str()
    '[10, 20, 5]'
    >>> lst.insere(1, 8)
    >>> lst.str()
    '[10, 8, 20, 5]'
    >>> lst.remove(2)
    >>> lst.str()
    '[10, 8, 5]'
    >>> lst.insere(lst.num_itens(), 8)
    >>> lst.str()
    '[10, 8, 5, 8]'
    >>> lst.indice(8)
    1
    >>> lst.remove_item(5)
    >>> lst.str()
    '[10, 8, 8]'
    '''
    valores: array[int]
    inicio: int
    fim: int
    tamanho: int 
    
    def __init__(self):
        ''' Cria uma nova lista vazia '''
        self.valores = array[CAPACIDADE_INICIAL]
        self.inicio = 0
        self.fim = 0
        self.tamanho = 0

    def num_itens(self) -> int:
        ''' Retorna a quantia de itens que a lista *self* possui '''
        return self.tamanho

    def get(self, i: int) -> int:
        ''' Retorna o número que está na posição *i* da lista'''
        if i < 0 or self.num_itens() <= i:
            raise ValueError(f'índice {i} fora da faixa')
        return self.valores[i]
    
    def set(self, i: int, n: int):
        ''' Troca o numero que está na posição *i* pelo item *n* '''
        if i < 0 or self.num_itens() <= i:
            raise ValueError(f'índice {i} fora da faixa')
        indice_real = (self.inicio + i) % len(self.valores)
        self.valores[indice_real] = n

    def appendRight(self, n: int):
        ''' Adiciona um valor *n* no fim da lista '''
        if self.cheia():
            raise ValueError('Lista cheia!')
        if self.vazia():
            self.valores[self.fim] = n
            self.fim += 1
            self.inicio = len(self.valores)
        else:
            self.valores[self.fim] = n
            if self.fim == len(self.valores):
                self.fim = 0
            else:
                self.fim += 1
        self.tamanho += 1
    
    def appendLeft(self, n: int):
        ''' Adiciona um valor *n* no inicio da lista '''
        if self.cheia():
            raise ValueError('Lista cheia!')
        if self.vazia():
            self.valores[self.inicio] = n
            self.fim += 1
            self.inicio = len(self.valores)
        else:
            self.valores[self.inicio] = n
            if self.inicio == 0:
                self.inicio = len(self.valores)
            else:
                self.inicio -= 1
        self.tamanho += 1

    def insere(self, i: int, n: int):
        ''' Adiciona um valor *n* no indice *i* da lista '''
        if self.cheia():
            raise ValueError('Lista cheia!')
        if i < 0 or i > self.num_itens():
            raise ValueError(f'indice {i} fora da faixa')
        indice_real = (self.inicio + i) % len(self.valores)
        if indice_real < self.num_itens() // 2:
            for j in range(self.inicio, indice_real):
                self.valores[j-1] = self.valores[j]
            if self.inicio == 0:
                self.inicio = len(self.valores)
            else:
                self.inicio -= 1
        else: # indice_real >= self.num_itens() // 2
            for j in range (self.fim, indice_real, -1):
                self.valores[j] = self.valores[j-1]
            if self.fim == len(self.valores):
                self.fim = 0
            else:
                self.fim += 1
        self.tamanho += 1
        self.valores[indice_real] = n
    
    def popRight(self) -> int:
        ''' Remove o valor do fim da lista '''
        if self.vazia():
            raise ValueError('Fila vazia!')
        if self.num_itens() - 1 <= len(self.valores) * 0.25:
            raise ValueError('Não é possivel reduzir a baixo de 25% da lista')
        if self.fim == 0:
            self.fim = len(self.valores)
        else:
            self.fim -= 1
        item = self.valores[self.fim]
        self.tamanho -= 1
        if self.num_itens() == 0:
            self.inicio = self.fim
        return item
    
    def popLeft(self) -> int:
        ''' Remove o valor do inicio da lista '''
        if self.vazia():
            raise ValueError('Fila vazia!')
        if self.num_itens() - 1 <= len(self.valores) * 0.25:
            raise ValueError('Não é possivel reduzir a baixo de 25% da lista')
        if self.inicio == len(self.valores):
            self.inicio = 0
        else:
            self.inicio += 1
        item = self.valores[self.inicio]
        self.tamanho -= 1
        if self.num_itens() == 0:
            self.fim == self.inicio
        return item

    def remove(self, i: int) -> int:
        ''' Remove um valor do indice *i* da lista '''
        if self.vazia():
            raise ValueError('Fila vazia!')
        if self.num_itens() - 1 <= len(self.valores) * 0.25:
            raise ValueError('Não é possivel reduzir a baixo de 25% da lista')
        if i < 0 or i > self.num_itens():
            raise ValueError(f'indice {i} fora da faixa')
        indice_real = (self.inicio + i) % len(self.valores)
        item = self.valores[indice_real]
        if indice_real < self.num_itens() // 2:
            for j in range(indice_real - 1, self.inicio, -1):
                self.valores[j] = self.valores[j-1]
            if self.inicio == 0:
                self.inicio = len(self.valores)
            else:
                self.inicio -= 1
        else: # indice_real >= self.num_itens() // 2
            for j in range (indice_real + 1, self.fim):
                self.valores[j-1] = self.valores[j]
            if self.fim == len(self.valores):
                self.fim = 0
            else:
                self.fim += 1
        return item
        

    
    def str(self) -> str:
        ''' Representa como uma string os elementos da lista '''
        s = '['
        if self.num_itens() != 0:
            s += str(self.valores[self.inicio])
            for i in range(1, self.num_itens()):
                s += ', ' + str(self.valores[i])
        return s + ']'
    
    def cheia(self) -> bool:
        ''' Verifica se a lista está cheia '''
        return self.fim + 1 == self.inicio or \
            self.fim == len(self.valores) and self.inicio == 0
    
    def vazia(self) -> bool:
        ''' Verifica se a lista está vazia '''
        return self.inicio == self.fim