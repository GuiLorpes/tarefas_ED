from __future__ import annotations
from dataclasses import dataclass


@dataclass
class Node:
    '''Um nó em um encadeamento'''
    item: str
    prioridade: int
    prox: Node | None


class Fila:
    '''
    Uma coleção de strings que segue a política FIFO: o primeiro a ser inserido
    é o primeiro a ser removido.

    Exemplos
    >>> f = Fila()
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
        Adiciona *item* no final da fila com uma prioridade de 1 a 5.
        '''
        assert prioridade > 0 and prioridade <= 5
        if self.fim is None:
            assert self.inicio is None
            self.inicio = Node(item, prioridade, None)
            self.fim = self.inicio
        else:
            self.fim.prox = Node(item, prioridade, None)
            self.fim = self.fim.prox

    def desenfileira(self) -> str | None:
        '''
        Remove e devolve o primeiro elemento com maior prioridade da fila.

        Requer que a fila não esteja vazia.
        '''
        if self.inicio is None:
            item = None
        else:
            q = self.inicio
            maior_pri = q
            while q.prox is not None and q.prox.prioridade < 5:
                if maior_pri.prox.prox.prioridade > maior_pri.prioridade:
                    maior_pri = maior_pri.prox
                q = q.prox
        return item

    def vazia(self) -> bool:
        '''
        Devolve True se a fila está vazia, False caso contrário.
        '''
        return self.inicio is None