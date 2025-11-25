from __future__ import annotations
from dataclasses import dataclass

@dataclass
class Node:
    esq: Node | None
    chave: int
    dir: Node | None

Arvore = Node | None

def abs_tree(t: Arvore) -> Arvore:
    '''
    Transforma os elementos de *t* para seus valores absolutos
    Exemplos
    >>> t1 = Node(None, -7, Node(None, 1, None))
    >>> t2 = Node(Node(None, 4, None), 8, t1)
    >>> t3 = Node(Node(None, -5, None), 6, Node(None, 9, None))
    >>> t4 = Node(t2, -4, t3)

             t4 -4
               /   \
            /         \
        t2 8           6 t3
         /   \       /   \
        4 t1 -7     -5    9
               \
                1

    >>> t4 = abs_tree(t4)
    >>> t4
    Node(esq=Node(esq=Node(esq=None, chave=4, dir=None), chave=8, dir=Node(esq=None, chave=7, dir=Node(esq=None, chave=1, dir=None))), chave=4, dir=Node(esq=Node(esq=None, chave=5, dir=None), chave=6, dir=Node(esq=None, chave=9, dir=None)))
    '''
    if t is None:
        return t
    else:
        t.chave = abs(t.chave)
        abs_tree(t.dir)
        abs_tree(t.esq)
        return t
    
def eh_abb(t: Arvore) -> bool:
    '''
    Verifica se *t* é uma Arvore Binária de Busca
    Exemplos:
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

    >>> eh_abb(t4)
    False
    >>> a1 = Node(Node(None, 1, None), 3, None)
    >>> a2 = Node(a1, 4, Node(None, 5, None))
    >>> a3 = Node(Node(None, 7, None), 8, Node(None,9,None))
    >>> a4 = Node(a2, 6, a3)

                 a4 6
                  /   \
               /         \
           a2 4           8 a3
            /   \       /   \
        a1 3     5     7     9
         /
        1
    >>> eh_abb(a4)
    True
    '''
    if t is None:
        return True
    else:
        if eh_abb(t.dir) and eh_abb(t.esq):
            if t.dir is not None:
                return t.dir.chave > t.chave
            elif t.esq is not None:
                return t.esq.chave < t.chave
            elif t.esq is not None and t.dir is not None:
                return t.dir.chave > t.chave and t.esq.chave < t.chave
            else:
                return True
        else:
            return False 

def eh_balanceada(t: Arvore) -> bool:
    '''
    Verifica se a altura das subarvores da direita e da esquerda de *t* diferem
    por no maximo 1, caso tenha, retorna True, caso a diferença entre elas for 
    maior que 1, retorna False
        Verifica se *t* é uma Arvore Binária de Busca
    Exemplos:
    >>> t1 = Node(None, 7, Node(None, 1, Node(None,3,None)))
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
                 \
                  3

    >>> eh_balanceada(t4)
    False
    >>> a1 = Node(Node(None, 1, None), 3, None)
    >>> a2 = Node(a1, 4, Node(None, 5, None))
    >>> a3 = Node(Node(None, 7, None), 8, Node(None,9,None))
    >>> a4 = Node(a2, 6, a3)

                 a4 6
                  /   \
               /         \
           a2 4           8 a3
            /   \       /   \
        a1 3     5     7     9
         /
        1

    >>> eh_balanceada(a4)
    True

    '''
    if t is None:
        return True
    else:
        return (abs(altura(t.dir) - altura(t.esq)) <= 1)

def altura(t: Arvore) -> int:
    '''
    Verifica a altura de uma arvore
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

    >>> altura(t4)
    3
    >>> altura(t3)
    1
    >>> altura(t2)
    2
    >>> altura(t1)
    1
    '''
    if t is None:
        return -1
    else:
        return max(altura(t.dir), altura(t.esq)) + 1
    
def sucessor(t: Arvore, n: int) -> int | None:
    '''
    Procura em *t* o menor valor maior que *n* e o retorna, caso não há, 
    retorna None
    Exemplos
    >>> a1 = Node(Node(None, 1, None), 3, None)
    >>> a2 = Node(a1, 4, Node(None, 5, None))
    >>> a3 = Node(Node(None, 7, None), 8, Node(None,9,None))
    >>> a4 = Node(a2, 6, a3)

                 a4 6
                  /   \
               /         \
           a2 4           8 a3
            /   \       /   \
        a1 3     5     7     9
         /
        1

    >>> sucessor(a4, 6)
    7
    >>> sucessor(a4,3) is None
    True
    >>> sucessor(a4,4)
    5
    '''
    if t is None:
        return None
    else:
        i = t
        while i.chave != n:
                if n > i.chave and i.dir is not None:
                    i = i.dir
                if n < i.chave and i.esq is not None:
                    i = i.esq
        if i.dir is None:
            return None
        else:
            i = i.dir
            while i.esq is not None:
                i = i.esq
            return i.chave
        
def amplitude(t: Arvore) -> int:
    '''
    >>> a1 = Node(Node(None, 1, None), 3, None)
    >>> a2 = Node(a1, 4, Node(None, 5, None))
    >>> a3 = Node(Node(None, 7, None), 8, Node(None,9,None))
    >>> a4 = Node(a2, 6, a3)

                 a4 6
                  /   \
               /         \
           a2 4           8 a3
            /   \       /   \
        a1 3     5     7     9
         /
        1

    >>> amplitude(a4)
    8
    >>> amplitude(a2)
    4
    >>> amplitude(a1)
    2
    >>> amplitude(a4)
    8
    '''
    if t is None:
        return 0
    else:
        min = t
        max = t
        while min.esq is not None:
            min = min.esq
        while max.dir is not None:
            max = max.dir
        return max.chave - min.chave