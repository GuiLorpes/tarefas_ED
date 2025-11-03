from __future__ import annotations
from dataclasses import dataclass

@dataclass
class Node:
    primeiro: int
    resto: Lista

Lista = Node | None

def tem_impar (lst: Lista) -> bool:
    ''' 
    Verifica se algum dos elementos da lista é impar 
    Exemplos
    >>> tem_impar(Node(2,Node(4,Node(5, None))))
    True
    >>> tem_impar(Node(3,Node(4,Node(0, None))))
    True
    >>> tem_impar(Node(2,Node(4,Node(6, None))))
    False
    >>> tem_impar(Node(2,Node(7,Node(6, None))))
    True
    >>> tem_impar(None)
    False
    '''
    return lst is not None and (lst.primeiro % 2 == 1 or tem_impar(lst.resto))

