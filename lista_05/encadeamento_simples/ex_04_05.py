from __future__ import annotations
from dataclasses import dataclass

@dataclass
class Node:
    ''' Um nó de inteiros '''
    item: int
    prox: Node | None

p = Node(7, None)
p.prox = Node(1, None)
p.prox.prox = Node(2, None)

def transforma_list_em_no(lst: list[int]) -> Node:
    '''
    Transforma uma lista em um encadeamento com ordem contrária
    Exemplos
    >>> transforma_list_em_no([1,2,3,4])
    Node(item=4, prox=Node(item=3, prox=Node(item=2, prox=Node(item=1, prox=None))))
    '''
    p = Node(lst[0], None)
    for i in range (1, len(lst)):
        q = Node(lst[i], p)
        p = q
    return p 

def elementos_em_no(p: Node | None) -> int:
    '''
    Determina quantos itens existem no encadeamento que começa com *p*
    Exemplos
    >>> elementos_em_no(None)
    0
    >>> elementos_em_no(Node(10,None))
    1
    >>> elementos_em_no(Node(10, Node(20, None)))
    2
    >>> elementos_em_no(Node(10, Node(20, Node(30, None))))
    3
    '''
    num_elementos = 0
    if p is not None:
        num_elementos = 1
        q = p
        while q.prox is not None:
            q = q.prox
            num_elementos += 1
    return num_elementos