from __future__ import annotations
from dataclasses import dataclass

# Árvore Binária de Busca

@dataclass
class Node:
    '''
    Um nó em uma árvore AVL
    '''
    esq: Arvore
    chave: int
    dir: Arvore

Arvore = Node | None

def busca(t: Arvore, chave: int) -> bool:
    ''' Procura pelo valor da *chave* em *self* e retorna se está na arvore ou não '''
    if t is None:
        return False
    elif chave == t.chave:
        return True
    elif chave < t.chave:
        return busca(t.esq, chave)
    else:  # val > t.val
        return busca(t.dir, chave)

def insere(t: Arvore, n: int) -> Node: # O(h)
    '''
    Devolve a raiz da ABB que é o resultado
    da inserção de *chave* em *t*.
    Se *chave* já está em *t*, devolve *t*.
    Requer que *t* seja uma ABB.
    Exemplo
    >>> r = None
    >>> r = insere(r, 10)
    >>> r
    Node(esq=None, chave=10, dir=None)
    '''
    if t is None:
        return Node(None, n, None)
    elif n < t.chave:
        t.esq = insere(t.esq, n)
    elif n > t.chave:
        t.dir = insere(t.dir, n)
    return t

def arvore_p_lista(t: Arvore) -> list[int]:  # O(h)
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

# Conjunto de ABB

class Conjunto:
    '''U
    m conjunto de números inteiros
    Exemplos
    >>> c1 = Conjunto()
    >>> c1.adiciona(2)
    >>> c1.adiciona(3)
    >>> c1.adiciona(4)
    >>> c1.mostra()
    '{2, 3, 4}'
    >>> c2 = Conjunto()
    >>> c2.adiciona(1)
    >>> c2.adiciona(2)
    >>> c2.adiciona(4)
    >>> c2.mostra()
    '{1, 2, 4}'
    >>> c3 = c1.uniao(c2)
    >>> c3.mostra()
    '{1, 2, 3, 4}'
    '''
    conjunto: Arvore

    def __init__(self) -> None:
        '''Cria um novo conjunto vazio.'''
        self.conjunto = None

    def adiciona(self, n: int) -> None: # Tempo de execução igual ao do insere, O(h)
        '''
        Adiciona *n* ao conjunto.
        
        Testes de propriedade

        * Ao inserir, a arvore precisa se manter em ABB *

        >>> import random
        >>> numeros = list(range(100))
        >>> random.shuffle(numeros)
        >>> c = Conjunto()
        >>> for n in numeros:
        ...     c.adiciona(n)
        >>> eh_abb(c.conjunto)
        True
        '''
        self.conjunto = insere(self.conjunto, n)

    def mostra(self) -> str: # O(n)
        '''
        Cria uma string com os elementos entre chaves e separados por vírgula.
        
        Testes de propriedade

        * A string sempre começa e termina com {}, nunca tem virgula antes do 
        primeiro e nem depois do ultimo, sempre tem virgula entre os numeros *

        >>> c = Conjunto()
        >>> str_correta(c.mostra())
        True
        >>> for i in range(100):
        ...     c.adiciona(i)
        >>> str_correta(c.mostra())
        True
        '''
        s = '{'
        for i in arvore_p_lista(self.conjunto):
            if s == '{':
                s += str(i)
            else:
                s+= ', ' + str(i)
        return s + '}'

    def uniao(self, outro: Conjunto) -> Conjunto: # O(h)
        '''
        Realiza a união entre *self* e *outro*.
        
        Teste de propriedade

        * Adicionou todos os elementos de A e B, e nenhum de fora *

        >>> A = Conjunto()
        >>> B = Conjunto()
        >>> for i in range (1, 6):
        ...     A.adiciona(i)
        >>> A.mostra()
        '{1, 2, 3, 4, 5}'
        >>> for i in range (6, 11):
        ...     B.adiciona(i)
        >>> B.mostra()
        '{6, 7, 8, 9, 10}'
        >>> C = A.uniao(B)
        >>> C.mostra()
        '{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}'
        >>> pertence_aos_conjuntos(A,B,C)
        True
        '''
        u = Conjunto()
        for i in arvore_p_lista(self.conjunto):
            u.adiciona(i)
        for i in arvore_p_lista(outro.conjunto):
            u.adiciona(i)
        return u
    
# Funções de verificação

def eh_abb(r: Arvore) -> bool: # O(h)
    return r is None or \
        (r.esq is None or r.esq.chave < r.chave and eh_abb(r.esq)) and \
        (r.dir is None or r.chave < r.dir.chave and eh_abb(r.dir))

def str_correta(s: str) -> bool: # O(1)
    '''
    Verifica se a string *s* está formatada corretamente, isto é:
    - Começa e termina com '{}'
    - Não possui ', ' antes do primeiro elemento e nem depois do último
    Exemplos
    >>> s = ['{', '}', '{}', '{, 1}', '{1, 2, }', '{1, 2, 3}']
    >>> str_correta(s[0])
    False
    >>> str_correta(s[1])
    False
    >>> str_correta(s[2])
    True
    >>> str_correta(s[3])
    False
    >>> str_correta(s[4])
    False
    >>> str_correta(s[5])
    True
    '''
    t = len(s)
    return (s[0] == '{' and s[-1] == '}') and (s[1:3] != ', ' and s[-3:-1] != ', ')

def pertence_aos_conjuntos(a: Conjunto, b: Conjunto, c: Conjunto) -> bool:
    ''' 
    Verifica se os valores do conjunto *a* e *b* estão no conjunto *c*. Caso 
    tenha algum valor não presente no conjunto, retorna False.
    '''
    pertenceA = False
    pertenceB = False
    for i in arvore_p_lista(a.conjunto):
        pertenceA = busca(c.conjunto, i)
    for i in arvore_p_lista(a.conjunto):
        pertenceB = busca(c.conjunto, i)
    return pertenceA and pertenceB
