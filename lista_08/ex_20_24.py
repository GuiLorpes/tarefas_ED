from __future__ import annotations
from dataclasses import dataclass

@dataclass
class Node:
    esq: Node | None
    chave: int
    dir: Node | None

Arvore = Node | None

def arvore_p_lista(t: Arvore) -> list[int]:
    '''
    Insere os valores de *t* em uma lista de forma ordenada, sem ordená-la
    Exemplo
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

    >>> arvore_p_lista(a4)
    [1, 3, 4, 5, 6, 7, 8, 9]
    '''
    if t is None:
        return []
    else:
        return arvore_p_lista(t.esq) + [t.chave] + arvore_p_lista(t.dir)
    
def arvore_p_lista_decrescente(t: Arvore) -> list[int]:
    '''
    Insere os valores de *t* em uma lista de forma decrescente, sem ordená-la
    Exemplo
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

    >>> arvore_p_lista_decrescente(a4)
    [9, 8, 7, 6, 5, 4, 3, 1]
    '''
    if t is None:
        return []
    else:
        return arvore_p_lista_decrescente(t.dir) + [t.chave] + \
            arvore_p_lista_decrescente(t.esq)

def lista_p_abb(lst: list[int]) -> Arvore:
    '''
    Cria uma árvore binaria de busca a partir dos itens de *lst*, sem usar a 
    função de inserir da árvore
    Exemplos
    >>> lista_p_abb([1, 3, 4, 5, 6, 7, 8, 9])
    Node(esq=Node(esq=Node(esq=Node(esq=None, chave=1, dir=None), chave=3, dir=None), chave=4, dir=Node(esq=None, chave=5, dir=None)), chave=6, dir=Node(esq=Node(esq=None, chave=7, dir=None), chave=8, dir=Node(esq=None, chave=9, dir=None)))
    
                    6
                  /   \
               /         \
              4           8
            /   \       /   \
           3     5     7     9
         /
        1

        '''
    if lst == []:
        return None
    else:
        e = lst[:(len(lst) // 2)]
        d = lst[(len(lst) // 2) + 1:]
        return Node(lista_p_abb(e), lst[(len(lst) // 2)], lista_p_abb(d))
    
def inserir_it(t:Arvore, n: int) -> Arvore:
    '''
    Insere *n* em *t*, de forma que *t* se mantenha uma árvore de busca
    Exemplo
    >>> t = lista_p_abb([1, 3, 4, 5, 6, 7, 8, 9])
        
                    6
                  /   \
               /         \
              4           8
            /   \       /   \
           3     5     7     9
         /
        1

    >>> t = inserir_it(t, 10)
    >>> t
    Node(esq=Node(esq=Node(esq=Node(esq=None, chave=1, dir=None), chave=3, dir=None), chave=4, dir=Node(esq=None, chave=5, dir=None)), chave=6, dir=Node(esq=Node(esq=None, chave=7, dir=None), chave=8, dir=Node(esq=None, chave=9, dir=Node(esq=None, chave=10, dir=None))))
        
                    6
                  /   \
               /         \
              4           8
            /   \       /   \
           3     5     7     9
         /                     \
        1                       10
    
    '''
    i = t
    while i is not None:
        if n == i.chave:
            return None
        else:
            if n > i.chave and i.dir is not None:
                i = i.dir
            elif n < i.chave and i.esq is not None:
                i = i.esq
            elif n > i.chave and i.dir is None:
                i.dir = Node(None, n, None)
                i = None
            elif i.esq is None and n < i.chave:
                i.esq = Node(None, n, None)
                i = None
    return t

def remover_it(t:Arvore, n: int) -> Arvore:
    '''
    Remove *n* em *t*, de forma que *t* se mantenha uma árvore de busca
    Exemplo
    >>> t = lista_p_abb([1, 3, 4, 5, 6, 7, 8, 9])
        
                    6
                  /   \
               /         \
              4           8
            /   \       /   \
           3     5     7     9
         /
        1

    >>> t = remover_it(t, 3)
    >>> t = remover_it(t, 8)
    >>> t
    Node(esq=Node(esq=Node(esq=None, chave=1, dir=None), chave=4, dir=Node(esq=None, chave=5, dir=None)), chave=6, dir=Node(Node(None, 7, None), chave=9, dir=None))
    '''
    raise NotImplementedError