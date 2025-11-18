from __future__ import annotations
from dataclasses import dataclass

@dataclass
class NodeS:
    primeiro: str
    resto: ListaS

ListaS = NodeS | None

@dataclass
class NodeI:
    primeiro: int
    resto: ListaI

ListaI = NodeI | None

def todos_tamanho_n (lst: ListaS, n: int):
    '''
    Transforma todos os itens de *lst* para ficarem com tamanho *n*
    Exemplo
    >>> 
    >>> l = NodeS('pica', NodeS('buceta', NodeS('Guilherme', None)))
    >>> todos_tamanho_n(l, 5)
    >>> l
    NodeS(primeiro='pica ', resto=NodeS(primeiro='bucet', resto=NodeS(primeiro='Guilh', resto=None)))
    '''
    if lst is None:
        pass
    else:
        if len(lst.primeiro) <= n:
            lst.primeiro += ' ' * (n - len(lst.primeiro))
        else:
            lst.primeiro = lst.primeiro[:n]
        todos_tamanho_n(lst.resto, n)

def potencia (a: int, n: int) -> int:
    '''
    Exemplos
    >>> potencia(3, 0)
    1
    >>> potencia(3, 4)
    81
    '''
    assert a != 0
    if n == 0:
        return 1
    else:
        return a * potencia(a, n-1)
    
def so_posi(lst: ListaI) -> ListaI:
    '''
    Cria a partir de *lst* uma nova lista com apenas os valores positivos de 
    *lst*
    >>> so_posi(NodeI(5,NodeI(-4,NodeI(-1,None))))
    NodeI(primeiro=5, resto=None)
    >>> so_posi(NodeI(5,NodeI(-4,NodeI(1,None))))
    NodeI(primeiro=5, resto=NodeI(primeiro=1, resto=None))
    >>> so_posi(NodeI(-5,NodeI(-4,NodeI(-1,None)))) is None
    True
    '''
    if lst is None:
        return None
    else:
        if lst.primeiro >= 0:
            return NodeI(lst.primeiro, so_posi(lst.resto))
        else:
            return so_posi(lst.resto)
        
def maior_length (lst: ListaS) -> int | None:
    '''
    Verifica qual é o maior tamanho de caracteres dos itens de *lst*. 
    Se *lst* for vazia, retorna None.
    Exemplo
    >>> maior_length(NodeS('pica', NodeS('buceta', NodeS('Guilherme', None))))
    9
    >>> maior_length(NodeS('pica', NodeS('buceta', NodeS('show', None))))
    6
    >>> maior_length(NodeS('pica', NodeS('woww', NodeS('show', None))))
    4
    >>> maior_length(None) is None
    True
    '''
    if lst is None:
        return None
    else:
        m = maior_length(lst.resto)
        if m is None:
            return len(lst.primeiro)
        elif m is not None and m >= len(lst.primeiro):
            return m
        else:
            return len(lst.primeiro)