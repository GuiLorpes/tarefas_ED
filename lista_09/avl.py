from __future__ import annotations
from dataclasses import dataclass


@dataclass
class No:
    '''
    Um nó em uma árvore AVL
    '''
    esq: Arvore
    chave: str
    dir: Arvore
    altura: int = 0


# Uma árvore AVL
Arvore = No | None


# Funções principais


def busca(r: Arvore, chave: str) -> bool:
    '''
    Devolve True se *chave* está em *r*, False caso contrário.

    Exemplos

    >>> r = insere(None, 'c')
    >>> r = insere(r, 'a')
    >>> r = insere(r, 'd')
    >>> busca(r, 'a')
    True
    >>> busca(r, 'b')
    False

    Teste de propriedade

    >>> r = None
    >>> for chave in range(0, 100, 2):
    ...     r = insere(r, str(chave))
    >>> for chave in range(0, 100, 2):
    ...     assert busca(r, str(chave)) == True, f'{chave} deveria estar na árvore!'
    >>> for chave in range(1, 100, 2):
    ...     assert busca(r, str(chave)) == False, f'{chave} não deveria estar na árvore!'
    '''
    if r is None:
        return False
    elif chave == r.chave:
        return True
    elif chave < r.chave:
        return busca(r.esq, chave)
    else:  # val > t.val
        return busca(r.dir, chave)


def insere(r: Arvore, chave: str) -> No:
    '''
    Devolve a raiz da árvore AVL que é o resultado da inserção de *chave* em
    *r*.

    Se *chave* já está em *r*, devolve *r*.

    Exemplos

    >>> r = insere(None, 'c')
    >>> r = insere(r, 'a')
    >>> r = insere(r, 'd')
    >>> busca(r, 'a')
    True
    >>> busca(r, 'b')
    False

    Testes de propriedade

    Nós testes a seguir, várias árvores são criadas pela inserção de elementos
    e após cada inserção é verificada se a árvore mantém a propriedade da AVL.

    >>> # Inserção em ordem
    >>> r = None
    >>> for chave in range(100):
    ...     r = insere(r, str(chave))
    ...     assert eh_avl(r) == True, 'deveria ser avl!'
    >>> # Inserção aleatória
    >>> import random
    >>> chaves = list(range(100))
    >>> random.shuffle(chaves)
    >>> r = None
    >>> for chave in chaves:
    ...     r = insere(r, str(chave))
    ...     assert eh_avl(r) == True, 'deveria ser avl'
    '''
    if r is None:
        return No(None, chave, None)
    elif chave < r.chave:
        r.esq = insere(r.esq, chave)
        r = balanceia_esq(r)
    elif chave > r.chave:
        r.dir = insere(r.dir, chave)
        r = balanceia_dir(r)
    return r


def remove(r: Arvore, chave: str) -> Arvore:
    '''
    Devolve a raiz da árvore AVL que é o resultado da remoção de *chave* em *r*.

    Se *chave* não está em *r*, devolve *r*.

    Se *r* só tem um nó e *chave* está nesse nó, devolve None.

    Exemplos

    >>> r = insere(None, 'g')
    >>> r = insere(r, 'd')
    >>> r = insere(r, 'b')
    >>> busca(r, 'b')
    True
    >>> r = remove(r, 'b')
    >>> busca(r, 'b')
    False


    Testes de propriedade

    Nos testes a seguir várias árvores são criadas, em seguida algumas chaves
    são removidas e a proprieade de AVL e o resultado de busca são verificados.

    >>> # Remoção em ordem
    >>> r = None
    >>> for chave in range(100):
    ...     r = insere(r, str(chave))
    >>> for chave in range(100):
    ...     r = remove(r, str(chave))
    ...     assert busca(r, str(chave)) == False, f'{chave} não deveria estar na árvore!'
    ...     assert eh_avl(r) == True, 'deveria ser avl!'
    >>> # Remoção aleatória
    >>> import random
    >>> chaves = list(range(100))
    >>> random.shuffle(chaves)
    >>> r = None
    >>> for chave in range(100):
    ...     r = insere(r, str(chave))
    >>> for chave in chaves:
    ...     r = remove(r, str(chave))
    ...     assert busca(r, str(chave)) == False, f'{chave} não deveria estar na árvore!'
    ...     assert eh_avl(r) == True, 'deveria ser avl!'
    '''
    if r is None:
        return None
    elif chave < r.chave:
        r.esq = remove(r.esq, chave)
        r.esq = balanceia_esq(r)
        return r
    elif chave > r.chave:
        r.dir = remove(r.dir, chave)
        r.dir = balanceia_dir(r)
        return r
    else:  # chave == r.chave
        if r.esq is None:
            # Se r.dir é None
            #  r     ->  None
            #
            # Se r.dir não é None
            # r           D
            #  \     ->  / \
            #   D       DE DD
            #  / \
            # DE DD
            return r.dir
        elif r.dir is None:
            #     r       r
            #    /   ->  / \
            #   E       EE ED
            #  / \
            # EE ED
            return r.esq
        else:
            # Tem os dois filhos
            #     r           r (chave=max)
            #    / \    ->   / \
            #   E   D       E   D
            #  com         sem
            #  max         max
            m = maximo(r.esq)
            r.chave = m
            r.esq = remove(r.esq, m)
            return r


# Funções auxiliares

def rotaciona_dir(r: No) -> No:
    '''
    Rotaciona a árvore com raiz *r* conforme o seguinte esquema:

        r            x
       / \          / \
      x   C   ->   A   r
     / \              / \
    A   B            B   C

    E devolve como nova raiz o nó que estava em *r.esq* quando a função foi
    chamada.

    Considerando que *r* é raiz de uma árvore AVL, então nas duas árvores
    A < r < B < x < C. Ou seja, a propriedade de ABB é preservada.

    O atributos altura dos nós da rotação são atualizados.

    Requer que *r.esq* não seja None.

    Testes

    >>> # Cria a árvore
    >>> #1 2  3  4  5
    >>> A, x, B, r, C = _cria_nos('12345')
    >>> r.esq, r.dir, r.altura = x, C, 2
    >>> x.esq, x.dir, x.altura = A, B, 1
    >>> # Chama a função
    >>> nr = rotaciona_dir(r)
    >>> # Verifica
    >>> nr is x
    True
    >>> r == No(B, '4', C, 1)
    True
    >>> x == No(A, '2', r, 2)
    True
    >>> A == No(None, '1', None, 0)
    True
    >>> B == No(None, '3', None, 0)
    True
    >>> C == No(None, '5', None, 0)
    True
    '''
    assert r.esq is not None
    x = r.esq
    r.esq = x.dir
    x.dir = r
    atualiza_altura(r)
    atualiza_altura(x)
    return x


def balanceia_dir(r: No) -> No:
    '''
    Verifica o balanceamento de *r*, considerando o caso da subárvore a
    direita com maior altura, e faz o rebalanceamento e atualização das
    alturas se necessário. Devolve a raiz da árvore balanceada.

    Requer que *r.dir* não seja None.

    O balanceamento é feito de acordo com os seguintes casos:

    Caso 1 - direita-direita

       r  <- rotaciona_esq       x
      / \\                     /   \
     A   x                    r     y
        / \\                 / \   / \
       B   y                A   B C   D
          / \
         C   D

    Testes

    >>> # Cria a árvore
    >>> #1 2  3  4  5  6  7
    >>> A, r, B, x, C, y, D = _cria_nos('1234567')
    >>> r.esq, r.dir = A, x
    >>> x.esq, x.dir = B, y
    >>> y.esq, y.dir = C, D
    >>> for n in [A, B, y, C, x, r, D]: atualiza_altura(n)
    >>> # Chama a função
    >>> nr = balanceia_dir(r)
    >>> # Verifica  
    >>> nr is x
    True
    >>> x == No(r, '4', y, 2)
    True
    >>> y == No(C, '6', D, 1)
    True
    >>> r == No(A, '2', B, 1)
    True
    >>> A == No(None, '1', None, 0)
    True
    >>> B == No(None, '3', None, 0)
    True
    >>> C == No(None, '5', None, 0)
    True
    >>> D == No(None, '7', None, 0)
    True


    Caso 2 - direita-esquerda

            r                               r  <- rotaciona_esq    y
          /   \\                           / \                   /   \
         A     x  <- rotaciona_dir   ->   A   y                 r     x
             // \                            / \               / \   / \
             y   D                          B   x             A   B C   D
            / \                                / \
           B   C                              C   D

           
    Teste

    >>> # Cria a árvore
    >>> # 1  2  3  4  5  6  7
    >>> A, r, B, y, C, x, D = _cria_nos('1234567')
    >>> r.esq, r.dir = A, x
    >>> x.esq, x.dir = y, D
    >>> y.esq, y.dir = B, C
    >>> for n in [A, B, y, C, x, r, D]: atualiza_altura(n)
    >>> # Chama a função
    >>> nr = balanceia_dir(r)
    >>> # Verifica
    >>> nr is y
    True
    >>> y == No(r, '4', x, 2)
    True
    >>> x == No(C, '6', D, 1)
    True
    >>> r == No(A, '2', B, 1)
    True
    >>> A == No(None, '1', None, 0)
    True
    >>> B == No(None, '3', None, 0)
    True
    >>> C == No(None, '5', None, 0)
    True
    >>> D == No(None, '7', None, 0)
    True
    '''
    assert r.dir is not None
    if altura(r.dir) - altura(r.esq) == 2:
        if altura(r.dir.dir) > altura(r.dir.esq):
            # Caso 1 - direta-direita
            return rotaciona_esq(r)
        else:
            # Caso 2 - direita-esquerda
            assert altura(r.dir.esq) > altura(r.dir.dir)
            r.dir = rotaciona_dir(r.dir)
            return rotaciona_esq(r)
    else:
        # r está balanceada
        atualiza_altura(r)
        return r


def rotaciona_esq(r: No) -> No:
    '''
    Rotaciona a árvore com raiz *r* conforme o seguinte esquema:

         r              x
        / \            / \
       A   x    ->    r   C
          / \        / \
         B   C      A   B

    E devolve como nova raiz o nó que estava em *r.dir* quando a função foi
    chamada.

    Considerando que *r* é raiz de uma árvore AVL, então nas duas árvores
    A < r < B < x < C. Ou seja, a propriedade de ABB é preservada.

    O atributos altura dos nós da rotação são atualizados.

    Requer que *r.dir* não seja None.

    Testes

    >>> # Cria a árvore
    >>> #1 2  3  4  5
    >>> A, r, B, x, C = _cria_nos('12345')
    >>> x.esq, x.dir, x.altura = B, C, 1
    >>> r.esq, r.dir, r.altura = A, x, 2
    >>> # Chama a função
    >>> nr = rotaciona_esq(r)
    >>> # Verifica
    >>> nr is x
    True
    >>> x == No(r, '4', C, 2)
    True
    >>> r == No(A, '2', B, 1)
    True
    >>> A == No(None, '1', None, 0)
    True
    >>> B == No(None, '3', None, 0)
    True
    >>> C == No(None, '5', None, 0)
    True
    '''
    assert r.dir is not None
    x = r.dir
    r.dir = x.esq
    x.esq = r
    atualiza_altura(r)
    atualiza_altura(x)
    return x


def balanceia_esq(r: No) -> No:
    '''
    Verifica o balanceamento de *r*, considerando o caso da subárvore a
    esquerda com maior altura, e faz o rebalanceamento e atualização das
    alturas se necessário. Devolve a raiz da árvore balanceada.

    Requer que *r.esq* não seja None.

    O balanceamento é feito de acordo com os seguintes casos:

    Caso 1 - esquerda-esquerda

           r  <- rotaciona_dir   x
         // \                  /   \
         x   D                y     r
       // \                  / \   / \
       y   C                A   B C   D
      / \
     A   B

    Testes

    >>> # Cria a árvore
    >>> # 1  2  3  4  5  6  7
    >>> A, y, B, x, C, r, D = _cria_nos('1234567')
    >>> r.esq, r.dir = x, D
    >>> x.esq, x.dir = y, C
    >>> y.esq, y.dir = A, B
    >>> for n in [A, B, y, C, x, r, D]: atualiza_altura(n)
    >>> # Chama a função
    >>> nr = balanceia_esq(r)
    >>> # Verifica
    >>> nr is x
    True
    >>> x == No(y, '4', r, 2)
    True
    >>> r == No(C, '6', D, 1)
    True
    >>> y == No(A, '2', B, 1)
    True
    >>> A == No(None, '1', None, 0)
    True
    >>> B == No(None, '3', None, 0)
    True
    >>> C == No(None, '5', None, 0)
    True
    >>> D == No(None, '7', None, 0)
    True


    Caso 2 - esquerda-direita

                        r            r  <- rotaciona_dir   y
                      // \          / \                  /   \
    rotaciona_esq ->  x   D        y   D                x     r
                    // \          / \                  / \   / \
                    A   y        x   C                A   B C   D
                       / \      / \
                      B   C    A   B


    Testes

    >>> # Cria a árvore
    >>> #1 2  3  4  5  6  7
    >>> A, x, B, y, C, r, D = _cria_nos('1234567')
    >>> r.esq, r.dir = x, D
    >>> x.esq, x.dir = A, y
    >>> y.esq, y.dir = B, C
    >>> for n in [A, B, y, A, x, D, r]: atualiza_altura(n)
    >>> # Chama a função
    >>> nr = balanceia_esq(r)
    >>> # Verifica
    >>> nr is y
    True
    >>> y == No(x, '4', r, 2)
    True
    >>> r == No(C, '6', D, 1)
    True
    >>> x == No(A, '2', B, 1)
    True
    >>> A == No(None, '1', None, 0)
    True
    >>> B == No(None, '3', None, 0)
    True
    >>> C == No(None, '5', None, 0)
    True
    >>> D == No(None, '7', None, 0)
    True
    '''
    assert r.esq is not None
    if altura(r.esq) - altura(r.dir) == 2:
        if altura(r.esq.esq) > altura(r.esq.dir):
            # Caso 1 - esquerda-esquerda
            return rotaciona_dir(r)
        else:
            # Caso 2 - esquerda-direita
            assert altura(r.esq.dir) > altura(r.esq.esq)
            r.esq = rotaciona_esq(r.esq)
            return rotaciona_dir(r)
    else:
        # r está balanceada
        atualiza_altura(r)
        return r


def maximo(r: No) -> str:
    '''
    Encontra o valor máximo em *r*.

    Exemplos

    >>> r = None
    >>> for val in [5, 1, 2, 7, 6, 3, 8, 4]:
    ...     r = insere(r, val)
    >>> maximo(r)
    8
    '''
    while r.dir is not None:
        r = r.dir
    return r.chave


def altura(r: Arvore) -> int:
    '''
    Devolve a altura da árvore *t*.
    Devolve -1 se *t* é None.
    '''
    if r is None:
        return -1
    else:
        return r.altura


def atualiza_altura(no: No):
    '''
    Atualiza a altura do *no*.
    Requer que a altura de *no.esq* e *no.dir* esteja corretas.
    '''
    no.altura = 1 + max(altura(no.esq), altura(no.dir))


def _cria_nos(chaves: str) -> list[No]:
    # Cria uma lista de nós com cada caractere de *chaves* sendo uma chave.
    # Esta função é utilizada para simplificar a criação dos testes.
    nos = []
    for chave in chaves:
        nos.append(No(None, chave, None))
    return nos


# Funções de verificação
#
# A função eh_avl é utilizada para os testes aleatórios de inserção e remoção.

def eh_avl(r: Arvore) -> bool:
    return eh_abb(r) and eh_balanceada(r) and altura_correta(r)


def eh_abb(r: Arvore) -> bool:
    return r is None or \
        (r.esq is None or r.esq.chave < r.chave and eh_abb(r.esq)) and \
        (r.dir is None or r.chave < r.dir.chave and eh_abb(r.dir))


def eh_balanceada(r: Arvore) -> bool:
    return r is None or \
        abs(altura(r.esq) - altura(r.dir)) <= 1 and \
        eh_balanceada(r.esq) and \
        eh_balanceada(r.dir)


def altura_correta(r: Arvore) -> bool:
    return r is None or \
        r.altura == 1 + max(altura(r.esq), altura(r.dir)) and \
        altura_correta(r.esq) and \
        altura_correta(r.dir)
