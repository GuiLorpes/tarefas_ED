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

def maior(lst: Lista) -> int | None:
    ''' 
    Encontra o maior elemento de *lst*, caso *lst* for vazia, retorna None
    Exemplos
    >>> maior(Node(2,Node(4,Node(5, None))))
    5
    >>> maior(None) is None
    True
    >>> maior(Node(3,Node(4,Node(4, None))))
    4
    >>> maior(Node(7,Node(4,Node(4, None))))
    7
    >>> maior(Node(4,Node(4,Node(4, None))))
    4
    '''
    if lst is None:
        return None
    else:
        m = maior(lst.resto)
        if m is None:
            return lst.primeiro
        elif m is not None and m >= lst.primeiro:
            return m
        else:
            return lst.primeiro

def repete(s: str, n: int) -> str:
    '''
    Repete *s* por *n* vezes sem utilizar multiplicação de string
    Exemplo
    >>> repete('gostosa', 4)
    'gostosagostosagostosagostosa'
    '''
    if n == 0:
        return ''
    else:
        return s + repete(s, n-1)
    
def conta_numero (lst: list[int], n: int) -> int:
    '''
    Conta quantas vezes *n* está em *lst*
    Exemplo
    >>> conta_numero ([1,2,4,6,2,5,9], 2)
    2
    >>> conta_numero ([1,2,4,6,2,5,9], 10)
    0
    >>> conta_numero ([1,2,4,6,2,5,9], 5)
    1
    '''
    if lst == []:
        return 0
    else:
        if lst[0] == n:
            return 1 + conta_numero(lst[1:], n)
        else:
            return conta_numero(lst[1:], n)