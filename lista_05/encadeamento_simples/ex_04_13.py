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

def transforma_list_em_no(lst: list[int]) -> Node | None:
    '''
    Transforma uma lista em um encadeamento com ordem contrária
    Exemplos
    >>> transforma_list_em_no([1,2,3,4])
    Node(item=4, prox=Node(item=3, prox=Node(item=2, prox=Node(item=1, prox=None))))
    >>> transforma_list_em_no([]) is None
    True
    '''
    p: Node | None = None
    for n in lst:
        p = Node(n, p)
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

def soma_no(p: Node | None) -> int:
    '''
    Detemina a soma dos itens que existem no encadeamento que começa com *p*
    Exemplos
    >>> soma_no(None)
    0
    >>> soma_no(Node(10,None))
    10
    >>> soma_no(Node(10, Node(20, None)))
    30
    >>> soma_no(Node(10, Node(20, Node(30, None))))
    60
    '''
    soma_elementos = 0
    if p is not None:
        soma_elementos = p.item
        q = p
        while q.prox is not None:
            q = q.prox
            soma_elementos += q.item
    return soma_elementos

def soma_1(p: Node | None):
    '''
    Aumenta em 1 os itens do encadeamento que começa com *p*
    Exemplos
    >>> soma_1(None)
    Traceback (most recent call last):
    ...
    ValueError: não há itens para somar 1
    >>> p = Node(0, Node(1, Node(2, None)))
    >>> soma_1(p)
    >>> p
    Node(item=1, prox=Node(item=2, prox=Node(item=3, prox=None)))
    '''
    if p is None:
        raise ValueError("não há itens para somar 1")
    p.item += 1
    q = p
    while q.prox is not None:
        q = q.prox
        q.item += 1

def maior_do_no(p: Node | None) -> int:
    '''
    Encontra o maior numero do encadeamento que começa com *p*
    Exemplos
    >>> maior_do_no(None)
    Traceback (most recent call last):
    ...
    ValueError: não há itens para comparar
    >>> maior_do_no(Node(10, Node(3, Node(2, None))))
    10
    >>> maior_do_no(Node(10, Node(30, Node(2, None))))
    30
    >>> maior_do_no(Node(10, Node(30, Node(200, None))))
    200
    '''
    if p is None:
        raise ValueError("não há itens para comparar")
    maior = p.item
    q = p
    while q.prox is not None:
        if q.prox.item > maior:
            maior = q.prox.item
        q = q.prox
    return maior

def add_no(p: Node | None, item: int) -> Node:
    '''
    Adiciona um nó novo no final do encadeamento iniciado em *p* com o *item* 
    no final
    >>> p = add_no(None, 3)
    >>> p
    Node(item=3, prox=None)
    >>> add_no(p, 2)
    Node(item=3, prox=Node(item=2, prox=None))
    '''
    if p is None:
        p = Node(item, None)
    else:
        q = p
        while q.prox is not None:
            q = q.prox
        q.prox = Node(item, None)
    return p

def encadeia_lista(lst: list[int]) -> Node | None:
    '''
    Cria um encadeamento a partir da *lst*
    Exemplos
    >>> encadeia_lista([1,2,3,4])
    Node(item=1, prox=Node(item=2, prox=Node(item=3, prox=Node(item=4, prox=None))))
    '''
    p = Node(0, None)
    q = p
    for n in lst:
        q.prox = Node(n, None)
        q = q.prox
    return p.prox

def copia(p: Node | None) -> Node | None:
    '''
    Cria e devolve uma copia do encadeamento que inicia em *p*
    Exemplos
    >>> p = Node(1, Node(2, Node(3, None)))
    >>> q = copia(p)
    >>> p.item = 5
    >>> p.prox.item = 7
    >>> p.prox.prox.item = 11
    >>> q
    Node(item=1, prox=Node(item=2, prox=Node(item=3, prox=None)))
    >>> p
    Node(item=5, prox=Node(item=7, prox=Node(item=11, prox=None)))
    >>> copia(None)
    '''
    copia = None
    if p is not None:
        copia = Node(p.item, None)
        q = p
        c = copia
        while q.prox is not None:
            c.prox = Node(q.prox.item, None)
            q = q.prox
            c = c.prox
    return copia

def duplica_nos(p: Node | None):
    '''
    Modifica o encadeamento que começa em *p* criando uma
    cópia de cada nó e colocando a cópia após o nó original
    no encadeamento.

    Exemplos
    >>> p = Node(1, Node(2, None))
    >>> duplica_nos(p)
    >>> p
    Node(item=1, prox=Node(item=1, prox=Node(item=2, prox=Node(item=2, prox=None))))
    >>> # A modificação do primeiro
    >>> # não pode alterar o segundo!
    >>> p.item = 20
    >>> p.prox.item
    1
    '''
    if p is None:
        raise ValueError('não foi possivel duplicar pois não há elementos')
    else:
        q: Node | None = p
        while q is not None:
            i = Node(q.item, q.prox)
            q.prox = i
            q = i.prox

