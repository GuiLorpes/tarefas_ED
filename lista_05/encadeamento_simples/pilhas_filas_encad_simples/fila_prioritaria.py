from __future__ import annotations
from dataclasses import dataclass


@dataclass
class Node:
    '''
    Um nó em um encadeamento com uma prioridade de 1 a 5, sendo 1 a menor 
    prioridade e 5 a maior
    '''
    item: str
    prioridade: int
    prox: Node | None


class FilaPriori:
    '''
    Uma coleção de strings que segue a política FIFO: o primeiro a ser inserido
    é o primeiro a ser removido.

    Exemplos
    >>> f = FilaPriori()
    >>> f.vazia()
    True
    >>> f.enfileira('Amanda',5)
    >>> f.enfileira('Fernando',2)
    >>> f.enfileira('Márcia',4)
    >>> f.vazia()
    False
    >>> f.desenfileira()
    'Amanda'
    >>> f.enfileira('Pedro',1)
    >>> f.enfileira('Alberto',3)
    >>> while not f.vazia():
    ...     f.desenfileira()
    'Márcia'
    'Alberto'
    'Fernando'
    'Pedro'
    '''

    # Invariantes:
    #   - Se inicio é None, então fim é None
    #   - Se inicio é um No, então fim é o nó no fim do encadeamento que começa
    #     em inicio
    inicio: Node | None
    fim: Node | None

    def __init__(self) -> None:
        '''Cria uma nova fila vazia'''
        self.inicio = None
        self.fim = None

    def enfileira(self, item: str, prioridade:int):
        '''
        Adiciona *item* na fila de maneira ordenada de acordo com uma 
        *prioridade* de 1 a 5.
        '''
        assert prioridade > 0 and prioridade < 6
        novo = Node(item, prioridade, None)
        # Fila vazia
        if self.fim is None:
            assert self.inicio is None
            self.inicio = novo
            self.fim = self.inicio
        # Fila não vazia
        else:
            p = self.inicio
            if prioridade > self.inicio.prioridade:
                novo.prox = self.inicio
                self.inicio = novo
            else:
                while p.prox is not None and p.prox.prioridade >= prioridade:
                    p = p.prox
                novo.prox = p.prox
                p.prox = novo
                if novo.prox is None:
                    self.fim = novo

    def desenfileira(self) -> str | None:
        '''
        Remove e devolve o primeiro elemento com maior prioridade da fila.

        Requer que a fila não esteja vazia.
        '''
        if self.inicio is None:
            item = None
        else:
            item = self.inicio.item
            self.inicio = self.inicio.prox
            if self.inicio is None:
                self.fim = None
        return item

    def vazia(self) -> bool:
        '''
        Devolve True se a fila está vazia, False caso contrário.
        '''
        return self.inicio is None