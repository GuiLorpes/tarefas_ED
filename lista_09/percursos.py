from __future__ import annotations
from dataclasses import dataclass


@dataclass
class No:
    esq: Arvore
    val: int
    dir: Arvore


Arvore = No | None


def exemplo() -> No:
    r'''
    Cria e devolve a raiz da seguinte árvore que é usada como exemplo
    nas demais funções:

        7
       / \
    x 6   4 y
     / \   \
    8   1   5
           /
          2
    '''
    x = No(No(None, 8, None), 6, No(None, 1, None))
    y = No(None, 4, No(No(None, 2, None), 5, None))
    return No(x, 7, y)


# Versões recursivas

def em_ordem_r(r: Arvore):
    r'''
    Exibe os valores de *r* usando um percurso em-ordem, isto é:
        - exibe em-ordem os valores *r.esq*.
        - exibe *r.val*
        - exibe em-ordem os valores *r.dir*.

    Exemplo

    >>> em_ordem_r(exemplo())
    8
    6
    1
    7
    4
    2
    5
    '''
    if r is not None:
        em_ordem_r(r.esq)
        print(r.val)
        em_ordem_r(r.dir)


def pre_ordem_r(r: Arvore):
    r'''
    Exibe os valores de *r* usando um percurso pre-ordem, isto é:
        - exibe *r.val*
        - exibe em pre-ordem os valores *r.esq*.
        - exibe em pre-ordem os valores *r.dir*.

    Exemplo

    >>> pre_ordem_r(exemplo())
    7
    6
    8
    1
    4
    5
    2
    '''
    if r is not None:
        print(r.val)
        pre_ordem_r(r.esq)
        pre_ordem_r(r.dir)


def pos_ordem_r(r: Arvore):
    r'''
    Exibe os valores de *r* usando um percurso pos-ordem, isto é:
        - exibe em pos-ordem os valores *r.esq*.
        - exibe *r.val*
        - exibe em pos-ordem os valores *r.dir*.

    Exemplo

    >>> pos_ordem_r(exemplo())
    8
    1
    6
    2
    5
    4
    7
    '''
    if r is not None:
        pos_ordem_r(r.esq)
        pos_ordem_r(r.dir)
        print(r.val)


# Versões iterativas

def em_ordem(r: Arvore):
    r'''
    Exibe os valores de *r* usando um percurso em-ordem, isto é:
        - exibe em-ordem os valores *r.esq*.
        - exibe *r.val*
        - exibe em-ordem os valores *r.dir*.

    A implementação é iterativa e usa uma pilha.

    Exemplo

    >>> em_ordem(exemplo())
    8
    6
    1
    7
    4
    2
    5
    '''
    pilha: list[Arvore | int] = [r]
    while pilha != []:
        tarefa = pilha.pop()
        if isinstance(tarefa, int):
            print(tarefa)
        elif isinstance(tarefa, No):
            pilha.extend([tarefa.dir, tarefa.val, tarefa.esq])


def pre_ordem(r: Arvore):
    r'''
    Exibe os valores de *r* usando um percurso pre-ordem, isto é:
        - exibe *r.val*
        - exibe em pre-ordem os valores *r.esq*.
        - exibe em pre-ordem os valores *r.dir*.

    A implementação é iterativa e usa uma pilha.

    Exemplo

    >>> pre_ordem(exemplo())
    7
    6
    8
    1
    4
    5
    2
    '''
    pilha: list[Arvore | int] = [r]
    while pilha != []:
        tarefa = pilha.pop()
        if isinstance(tarefa, int):
            print(tarefa)
        elif isinstance(tarefa, No):
            pilha.extend([tarefa.dir, tarefa.esq, tarefa.val])


def pos_ordem(r: Arvore):
    r'''
    Exibe os valores de *r* usando um percurso pos-ordem, isto é:
        - exibe em pos-ordem os valores *r.esq*.
        - exibe *r.val*
        - exibe em pos-ordem os valores *r.dir*.

    A implementação é iterativa e usa uma pilha.

    Exemplo

    >>> pos_ordem(exemplo())
    8
    1
    6
    2
    5
    4
    7
    '''
    pilha: list[Arvore | int] = [r]
    while pilha != []:
        tarefa = pilha.pop()
        if isinstance(tarefa, int):
            print(tarefa)
        elif isinstance(tarefa, No):
            pilha.extend([tarefa.val, tarefa.dir, tarefa.esq])
