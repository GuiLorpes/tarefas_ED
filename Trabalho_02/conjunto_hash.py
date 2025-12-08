from __future__ import annotations
from dataclasses import dataclass

@dataclass
class Celula:
    chave: int
    valor: int

class Conjunto:
    '''
    Um conjunto de números inteiros
    Exemplos
    >>> c1 = Conjunto(10)
    >>> c1.adiciona(2)
    >>> c1.adiciona(3)
    >>> c1.adiciona(4)
    >>> c1.mostra()
    '{2, 3, 4}'
    >>> c2 = Conjunto(10)
    >>> c2.adiciona(1)
    >>> c2.adiciona(2)
    >>> c2.adiciona(4)
    >>> c2.mostra()
    '{1, 2, 4}'
    >>> c3 = c1.uniao(c2)
    >>> c3.mostra()
    '{1, 2, 3, 4}'
    '''
    conjunto: list[Celula | None]
    num_itens: int

    def __init__(self, m: int):
        self.conjunto = [None] * m
        self.num_itens = 0

    def busca(self, n: int) -> int | None:
        ''' 
        Procura pelo valor da *chave* em *self* e o retorna, se *chave* não
        estiver em *self*, retornar nada
        '''
        p = hash(n) % len(self.conjunto)
        t = self.conjunto[p]
        while t is not None:
            if isinstance(t, Celula):
                if t.chave == n:
                    return t.valor
            p = (p + 1) % len(self.conjunto)
            t = self.conjunto[p]
        return None

    def adiciona(self, n: int) -> None: 
        '''
        Adiciona *n* ao conjunto.

        Testes de propriedade
        
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
        '''
        p = hash(n) % len(self.conjunto)
        t = self.conjunto[p]
        while t is not None:
            if isinstance(t, Celula):
                if t.chave == n:
                    return None
            p = (p + 1) % len(self.conjunto)
            t = self.conjunto[p]
        self.conjunto[p] = Celula(n, n)
        self.num_itens += 1
        if self.num_itens == len(self.conjunto):
            self.conjunto = self.__aumenta()
        # O(1) ou O(n), depende de onde está e O(n) para realocar em um 
        # conjunto maior

    def mostra(self) -> str:
        '''
        Cria uma string com os elementos entre chaves e separados por vírgula.
        
        Testes de propriedade

        * A string sempre começa e termina com {}, nunca tem virgula antes do 
        primeiro e nem depois do ultimo, sempre tem virgula entre os numeros *

        >>> c = Conjunto(10)
        >>> str_correta(c.mostra())
        True
        >>> for i in range(100002):
        ...     c.adiciona(i)
        >>> str_correta(c.mostra())
        True
        '''
        s = '{'
        for i in range (len(self.conjunto)):
            t = self.conjunto[i]
            if isinstance(t, Celula):
                if s == '{':
                    s += str(t.valor)
                else:
                    s += ', ' + str(t.valor)
        else:
            return s + '}'
        # O(n)

    def uniao(self, outro: Conjunto) -> Conjunto:
        '''
        Realiza a união entre *self* e *outro*.
        
        Teste de propriedade

        * Adicionou todos os elementos de A e B, e nenhum de fora *

        >>> A = Conjunto(20)
        >>> B = Conjunto(20)
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
        t = len(self.conjunto) + len(outro.conjunto)
        u = Conjunto(t)
        for i in self.conjunto:
            if isinstance(i, Celula):
                u.adiciona(i.valor)
        for i in outro.conjunto:
            if isinstance(i, Celula):
                u.adiciona(i.valor)
        return u
        # O(n)
    
    def __aumenta(self) -> list[Celula | None]:
        '''
        Cria um conjunto 1.66x o tamanho do conjunto original quando ele está 
        cheio e o realoca para o novo conjunto. Se for impar adiciona mais um
        para ficar inteiro.
        Exemplos
        >>> c = Conjunto(1)
        >>> len(c.conjunto)
        1
        >>> c.adiciona(9)
        >>> len(c.conjunto)
        3
        '''
        aumento = 1.66
        tamanho_original = len(self.conjunto)
        tamanho_novo = (aumento * (tamanho_original + 1)) // 1 
        nc = Conjunto(int(tamanho_novo)) 
        for i in self.conjunto:
            if isinstance(i, Celula):
              nc.adiciona(i.valor)
        return nc.conjunto
        # O(n)

# Funções de verificação

def str_correta(s: str) -> bool:
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
    Verifica se os valores do conjunto *c* estão pelo menos em um dos conjuntos
    *a* ou *b*. Caso tenha algum valor não presente nesses dois conjuntos, 
    retorna False.
    '''
    pertence = False
    for i in c.conjunto:
        if isinstance(i, Celula):
            if (a.busca(i.chave) is not None) or (b.busca(i.chave) is not None):
                pertence = True
            else:
                pertence = False 
    return pertence
