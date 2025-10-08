from __future__ import annotations
from dataclasses import dataclass

@dataclass
class Node:
    '''Um nó em um encadeamento'''
    item: str
    prox: Node | None

class Fila:
    '''
    Uma coleção de strings que segue a política FIFO: o primeiro a ser inserido
    é o primeiro a ser removido.

    Exemplos
    >>> f = Fila()
    >>> f.vazia()
    True
    >>> f.enfileira('Amanda')
    >>> f.enfileira('Fernando')
    >>> f.enfileira('Márcia')
    >>> f.vazia()
    False
    >>> f.desenfileira()
    'Amanda'
    >>> f.vazia()
    False
    >>> f.enfileira('Pedro')
    >>> f.enfileira('Alberto')
    >>> while not f.vazia():
    ...     f.desenfileira()
    'Fernando'
    'Márcia'
    'Pedro'
    'Alberto'
    >>> f.vazia()
    True
    >>> f.enfileira('Guilherme')
    >>> f.vazia()
    False
    >>> f.desenfileira()
    'Guilherme'
    '''
    inicio: Node | None
    fim: Node | None

    def __init__(self) -> None:
        self.inicio = None
        self.fim = None

    def enfileira(self, item: str):
        if self.fim is None:
            self.inicio = Node(item, None)
            self.fim = self.inicio
        else:
            self.fim.prox = Node(item, None)
            self.fim = self.fim.prox

    def desenfileira(self) -> str:
        if self.inicio is None:
            raise ValueError('fila vazia')
        # Não atualiza o self.fim, caso for o ultimo elemento, gera um erro
        # Para corrigir deve-se verificar se o inicio é None e atualizar o 
        # fim para None também
        item = self.inicio.item
        self.inicio = self.inicio.prox
        return item
    
    def vazia(self) -> bool:
        return self.inicio is None