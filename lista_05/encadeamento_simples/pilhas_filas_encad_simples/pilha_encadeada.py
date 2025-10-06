from __future__ import annotations
from dataclasses import dataclass


@dataclass
class Node:
    '''Um nó em um encadeamento'''
    item: str
    prox: Node | None


class Pilha:
    '''
    Uma coleção de strings que segue a política LIFO: o elemento mais
    recentemente inserido é o primeiro a ser removido.

    >>> p = Pilha()
    >>> p.vazia()
    True
    >>> p.desempilha()
    'None'
    >>> p.empilha('O')
    >>> p.empilha('que')
    >>> p.empilha('escrever?')
    >>> p.vazia()
    False
    >>> p.desempilha()
    'escrever?'
    >>> p.empilha('fazer')
    >>> p.empilha('agora?')
    >>> p.inverte()
    >>> while not p.vazia():
    ...     p.desempilha()
    'O'
    'que'
    'fazer'
    'agora?'
    '''

    topo: No | None

    def __init__(self) -> None:
        '''
        Cria uma pilha vazia
        '''
        self.topo = None

    def empilha(self, item: str):
        '''
        Adiciona o *item* na pilha.
        '''
        self.topo = No(item, self.topo)

    def desempilha(self) -> str:
        '''
        Devolve o elemento mais recentemente adicionado da pilha.

        Requer que a pilha não esteja vazia.
        '''
        if self.topo is None:
            i = 'None'
        else:
            i = self.topo.item
            self.topo = self.topo.prox
        return i

    def vazia(self) -> bool:
        '''
        Devolve True se a pilha está vazia, False caso contrário.
        '''
        return self.topo is None
    
    def inverte(self) -> None:
        '''
        Inverte a ordem dos elementos da pilha
        '''
        raise NotImplementedError