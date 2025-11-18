from __future__ import annotations
from dataclasses import dataclass

# def impar (n: int) -> bool:

# def par (n: int) -> bool:

def eh_crescente (lst: list[int]) -> bool:
    '''
    Verifica se os elementos de *lst* estão em ordem não decrescente
    Exemplos
    >>> eh_crescente([])
    True
    >>> eh_crescente([1,4,4,7,8,10])
    True
    >>> eh_crescente([2,5,6,5,20])
    False
    >>> eh_crescente([1,1,1,1,1,1])
    True
    '''
    if lst == []:
        return True
    else:
        