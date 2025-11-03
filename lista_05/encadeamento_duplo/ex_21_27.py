from __future__ import annotations
from dataclasses import dataclass

@dataclass
class Node:
    ante: Node | None
    item: int
    prox: Node | None

# Ex 21

def list_para_node(lst: list[int]) -> Node | None:
    '''
    Transforma *lst* para um nó com os mesmos elementos da lista em ordem que 
    eles aparecem
    Exemplos
    >>> list_para_node([]) is None
    True
    >>> list_para_node([2,3,6])
    Node(ante=None, item=2, prox=Node(ante=..., item=3, prox=Node(ante=..., item=6, prox=None)))
    '''
    p = Node(None, 0, None)
    q = p
    for n in lst:
        q.prox = Node(q, n, None)
        q = q.prox
    if p.prox is not None:
        p.prox.ante = None  # mypy ta reclamando
    return p.prox

# Ex 22

def list_para_node_inv(lst: list[int]) -> Node | None:
    '''
    Transforma *lst* para um nó com os mesmos elementos da lista em ordem 
    invertida
    Exemplos
    >>> list_para_node_inv([]) is None
    True
    >>> list_para_node_inv([2,3,6])
    Node(ante=None, item=6, prox=Node(ante=..., item=3, prox=Node(ante=..., item=2, prox=None)))
    '''
    p: Node | None = None
    q = p
    for n in lst:
        novo = Node(None, n, p)
        if p is not None:
            p.ante = novo
        p = novo
    return p

# Ex 23

def troca_prox_ante(no: Node | None):
    '''
    Troca de lugar o *no*, cujo proximo é diferente de None, com o proximo dele
    Exemplos
    >>> p = Node(None, 4, Node(..., 3, Node(..., 12, None)))
    >>> troca_prox_ante(p)
    >>> p
    Node(ante=None, item=3, prox=Node(ante=..., item=12, prox=Node(ante=..., item=4, prox=None)))
    >>> troca_prox_ante(p.prox)
    >>> p
    Node(ante=None, item=3, prox=Node(ante=..., item=4, prox=Node(ante=..., item=12, prox=None)))
    '''
    