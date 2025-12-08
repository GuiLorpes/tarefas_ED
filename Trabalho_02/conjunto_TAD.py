from __future__ import annotations

class Conjunto:
    '''
    Um conjunto de números inteiros
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
    
    def __init__(self) -> None:
        '''Cria um novo conjunto vazio.'''
        raise NotImplementedError
    
    def adiciona(self, n: int) -> None:
        '''
        Adiciona *n* ao conjunto.

        Testes de propriedade para a tabela de disperção
        
        * Só adiciona um numero uma vez *

        >>> c = Conjunto(5)
        >>> for _ in range(10):
        ...      c.adiciona(2)
        >>> c.mostra()
        '{2}'
        >>> len(c.conjunto)
        5

        - Não adicionou mais de uma vez o numero, logo não precisou aumentar o 
        tamanho do conjunto -

        * O numero de itens do conjunto nunca é maior que o tamanho do conjunto *

        >>> for i in range(1000):
        ...     c.adiciona(i)
        >>> c.num_itens <= len(c.conjunto)
        True

        Teste de propriedade para a árvore de busca binária

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
        raise NotImplementedError
    
    def mostra(self) -> str:
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
        raise NotImplementedError
    
    def uniao(self, outro: Conjunto) -> Conjunto:
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
        raise NotImplementedError

# Funções de verificação

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
    raise NotImplementedError

def pertence_aos_conjuntos(a: Conjunto, b: Conjunto, c: Conjunto) -> bool:
    ''' 
    Verifica se os valores do conjunto *a* e *b* estão no conjunto *c*. Caso 
    tenha algum valor não presente no conjunto, retorna False.
    '''
    raise NotImplementedError