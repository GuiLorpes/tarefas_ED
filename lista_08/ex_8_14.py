from __future__ import annotations
from dataclasses import dataclass

'''

Desenho da arvore binaria com os elementos 3,6,8,20,21,22,23,30,40,46,50,60

                  22   
               /      \ 
           /              \ 
          8               40
        /   \           /    \
       6     20        30    50
      /        \      /     /   \
     3         21    23    46   60

'''

@dataclass
class Node:
    esq: Node | None
    chave: int
    dir: Node | None

Arvore = Node | None

def qtd_elementos (t: Arvore) -> int:
    '''
    Percorre *t* contando os elementos
    Exemplos
    >>> t1 = Node(None, 7, Node(None, 1, None))
    >>> t2 = Node(Node(None, 4, None), 8, t1)
    >>> t3 = Node(Node(None, 5, None), 6, Node(None,9,None))
    >>> t4 = Node(t2, 4, t3)

              t4 4
               /   \
            /         \
        t2 8           6 t3
         /   \       /   \
        4  t1 7     5     9
               \
                1

    >>> qtd_elementos(t4)
    8
    '''
    if t is None:
        return 0
    else:
        return 1 + qtd_elementos(t.esq) + qtd_elementos(t.dir)
    
def qtd_grau2 (t: Arvore) -> int:
    '''
    >>> t1 = Node(None, 7, Node(None, 1, None))
    >>> t2 = Node(Node(None, 4, None), 8, t1)
    >>> t3 = Node(Node(None, 5, None), 6, Node(None,9,None))
    >>> t4 = Node(t2, 4, t3)

              t4 4
               /   \
            /         \
        t2 8           6 t3
         /   \       /   \
        4  t1 7     5     9
               \
                1

    >>> qtd_grau2(t4)
    3
    '''
    if t is None:
        return 0
    else:
        if t.dir is not None and t.esq is not None:
            return 1 + qtd_grau2(t.dir) + qtd_grau2(t.esq)
        return qtd_grau2(t.dir) + qtd_grau2(t.esq)
        
def eh_cheia(t: Arvore) -> bool:
    '''
    Verifica se *t* é cheia ou não
    Exemplos
    >>> t1 = Node(None, 7, Node(None, 1, None))
    >>> t2 = Node(Node(None, 4, None), 8, t1)
    >>> t3 = Node(Node(None, 5, None), 6, Node(None,9,None))
    >>> t4 = Node(t2, 4, t3)

              t4 4
               /   \
            /         \
        t2 8           6 t3
         /   \       /   \
        4  t1 7     5     9
               \
                1

    >>> eh_cheia(t4)
    False
    >>> a1 = Node(None, 7, None)
    >>> a2 = Node(Node(None, 4, None), 8, a1)
    >>> a3 = Node(Node(None, 5, None), 6, Node(None,9,None))
    >>> a4 = Node(a2, 4, a3)

              a4 4
               /   \
            /         \
        a2 8           6 a3
         /   \       /   \
        4  a1 7     5     9

    >>> eh_cheia(a4)
    True
    '''
    if t is None:
        return True
    else:
        return ((t.dir is not None and t.esq is not None) or \
            (t.dir is None and t.esq is None)) and \
                (eh_cheia(t.dir) and eh_cheia(t.esq))
    
# def