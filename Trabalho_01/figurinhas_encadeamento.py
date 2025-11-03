from __future__ import annotations
from dataclasses import dataclass

@dataclass
class NodeD:
    ''' Um nó em um encadeamento duplo'''
    ante: NodeD | None
    item: Figurinha
    prox: NodeD | None

@dataclass
class NodeS:
    '''Um nó em um encadeamento simples'''
    item: int
    prox: NodeS | None


class Fila:
    '''
    Uma coleção de strings que segue a política FIFO: o primeiro a ser inserido
    é o primeiro a ser removido.

    Exemplos
    >>> f = Fila()
    >>> f.vazia()
    True
    >>> f.enfileira(1)
    >>> f.enfileira(2)
    >>> f.enfileira(3)
    >>> f.vazia()
    False
    >>> f.desenfileira()
    1
    >>> f.enfileira(4)
    >>> f.enfileira(5)
    >>> while not f.vazia():
    ...     f.desenfileira()
    2
    3
    4
    5
    '''

    # Invariantes:
    #   - Se inicio é None, então fim é None
    #   - Se inicio é um No, então fim é o nó no fim do encadeamento que começa
    #     em inicio
    inicio: NodeS | None
    fim: NodeS | None
    tamanho: int

    def __init__(self) -> None:
        '''Cria uma nova fila vazia'''
        self.inicio = None
        self.fim = None
        self.tamanho = 0

    def enfileira(self, item: int):
        '''
        Adiciona *item* no final da fila.
        '''
        if self.fim is None:
            assert self.inicio is None
            self.inicio = NodeS(item, None)
            self.fim = self.inicio
        else:
            self.fim.prox = NodeS(item, None)
            self.fim = self.fim.prox
        self.tamanho += 1

    def desenfileira(self) -> int | None:
        '''
        Remove e devolve o primeiro elemento da fila.

        Requer que a fila não esteja vazia.
        '''
        if self.inicio is None:
            item = None
        else:
            item = self.inicio.item
            self.inicio = self.inicio.prox
            if self.inicio is None:
                self.fim = None
        self.tamanho -= 1
        return item

    def vazia(self) -> bool:
        '''
        Devolve True se a fila está vazia, False caso contrário.
        '''
        return self.inicio is None
    
    def junta(self, b: Fila):
        '''
        Move todos os elementos da fila *b* para o final da fila *self*.
        Se a fila *self* estiver vazia, adiciona ela
        Exemplos
        >>> a = Fila()
        >>> a.enfileira(3)
        >>> a.enfileira(3)
        >>> b = Fila()
        >>> b.enfileira(4)
        >>> b.enfileira(4)
        >>> a.junta(b)
        >>> while not a.vazia():
        ...     a.desenfileira()
        3
        3
        4
        4
        '''
        if self.fim is None:
            assert self.inicio is None
            self.fim = b.inicio
        else:
            self.fim.prox = b.inicio

    def show_f(self) -> str:
        q = self.inicio
        if self.vazia():
            r = '[]'
        else:
            r = '['
            while q is not None:
                r += str(q.item)
                q = q.prox
                if q is not None:
                    r += ', '
            r += ']'
        return r 
    
@dataclass
class Figurinha:
    ''' 
    Representa uma figurinha de uma coleção, com sua identificação e a quantia 
    de cartas repetidas 
    '''
    numero: int
    quantia: int

class AlbumFigs:
    ''' 
    Um álbum de figurinhas onde cada figurinha é um inteiro positivo.
    Exemplos
    >>> a = AlbumFigs(300)
    >>> a.vazio()
    True
    >>> a.show()
    '[]'
    >>> a.add_fig(3)
    >>> a.add_fig(3)
    >>> a.add_fig(1)
    >>> a.add_fig(1)
    >>> a.add_fig(45)
    >>> a.add_fig(400)
    >>> a.show()
    '[1, 3, 45]'
    >>> a.show_rep()
    '[1 (1), 3 (1)]'
    >>> a.rm_fig(1)
    1
    >>> a.rm_fig(45)
    45
    >>> a.rm_fig(500)
    >>> a.show()
    '[1, 3]'
    >>> a.show_rep()
    '[3 (1)]'
    ''' 
    inicio: NodeD | None
    fim: NodeD | None
    figurinhas_na_colecao: int
    
    
    # Métodos

    def __init__(self, c: int):
        ''' 
        Cria um novo álbum com *c* figurinhas diferentes.
        '''
        self.inicio = None
        self.fim = None
        self.figurinhas_na_colecao = c

    # Verificar se a figurinha a ser inserida ou retirada está na coleção
    def no_intervalo(self, fig:int) -> bool:
        ''' Verifica se o valor de *fig* está na coleção do album *self* '''
        return fig > 0 and fig <= self.figurinhas_na_colecao
    
    def add_fig(self, fig:int):
        '''
        Se *fig* estiver no álbum, a quantidade dela é aumentada em 1.
        Caso contrário, *fig* é adicionada ao álbum com quantidade 1.
        Nada acontece se *fig* não estiver no intervalo de figurinhas possíveis do álbum.
        '''
        if self.no_intervalo(fig):
            if self.fim is None:
                assert self.inicio is None
                self.inicio = NodeD(None, (Figurinha(fig, 1)), None)
                self.fim = self.inicio
            else:
                if self.inicio is not None:
                    ii = self.inicio.item.numero
                    ie = self.fim.item.numero
                    # Adicionar no inicio ou no fim
                    if fig < ii:
                        novo = NodeD(None, Figurinha(fig, 1),self.inicio)
                        self.inicio.ante = novo
                        self.inicio = self.inicio.ante
                    elif fig > ie:
                        self.fim.prox = NodeD(self.fim, Figurinha(fig, 1),None)
                        self.fim = self.fim.prox
                # Insere no meio
                    else:
                        q = self.inicio
                        # Percorre o encadeamento até achar um nó com a figurinha maior ou igual a *fig*
                        while (q.prox is not None) and (q.item.numero < fig):
                            q = q.prox
                        # Se a figurinha for igual, adiciona 1 na quantia dela
                        if q is not None and q.item.numero == fig:
                            q.item.quantia += 1
                        # Se for maior que *fig*, adiciona antes dela
                        else:
                            novo = NodeD(q.ante, Figurinha(fig, 1),q)
                            if q.ante is not None:
                                q.ante.prox = novo
                            q.ante = novo
                        
    def rm_fig(self, fig:int) -> int | None:
        '''
        Se *fig* estiver no álbum, a quantidade dela é diminuida em 1 e, caso sua quantidade chegue
        a zero, ela é removida do álbum.
        Caso contrário, nada acontece.
        Nada acontece se *fig* não estiver no intervalo de figurinhas possíveis do álbum.
        Exemplos
        >>> a = AlbumFigs(20)
        >>> a.rm_fig(2)
        Traceback (most recent call last):
        ...
        ValueError: Album vazio
        >>> a.add_fig(10)
        >>> a.add_fig(2)
        >>> a.add_fig(2)
        >>> a.show_rep()
        '[2 (1)]'
        >>> a.show()
        '[2, 10]'
        >>> a.rm_fig(2)
        2
        >>> a.rm_fig(10)
        10
        >>> a.show()
        '[2]'
        '''
        if self.inicio is None:
            raise ValueError('Album vazio')
        
        figurinha: int | None = None
        if self.no_intervalo(fig):
            q:NodeD = self.inicio
            while self.no_intervalo(fig) and (q.prox is not None) and \
                    q is not None and q.item.numero != fig:
                q = q.prox
            if q is not None and q.item.numero == fig:
                figurinha = q.item.numero
                q.item.quantia -= 1
                # Remove nó quando quantia chegar a 0
                if q.prox is None and q.item.quantia == 0:
                    # Se só houver um item no album
                    if self.fim == self.inicio:
                        self.fim = None
                        self.inicio = None
                    # Se estiver no fim
                    elif q == self.fim:
                        self.fim = q.ante
                        if self.fim is not None:
                            self.fim.prox = None
                    # Remove de qualquer outro lugar
                    else:
                        if q.prox is not None:
                            q.prox.ante = q.ante
                        if q.ante is not None:
                            q.ante.prox = q.prox
        return figurinha
    
    def show(self) -> str:
        '''
        Mostra todos as figurinhas do album sem mostrar as quantias de cada
        '''
        q = self.inicio
        if self.inicio is None:
            r = '[]'
        else:
            r = '['
            while q is not None:
                r += str(q.item.numero)
                q = q.prox
                if q is not None:
                    r  += ', '
            r += ']'
        return r 

    def show_rep(self) -> str:
        '''
        Mostra todas as figurinhas repetidas e sua quantidade
        '''
        q = self.inicio
        if self.vazio():
            r = '[]'
        else:
            r = '['
            tem_repetida = False
            # Adiciona até o penultimo
            while q is not None:
                if q.item.quantia > 1:
                    if tem_repetida:
                        r += ', '
                    r += str(q.item.numero) + ' (' + str(q.item.quantia - 1) + ')'
                    tem_repetida = True
                q = q.prox
            # Ultimo tem repetida
            r += ']' 
        return r 
    
    def trocas_maximas(self, b: AlbumFigs):
        '''
        Verifica quantas cartas de *self* é possivel trocar com *b*, e troca em
        pares as cartinhas dos dois albuns, caso não seja possivel realizar 
        nenhuma troca, não faz nada.
        Exemplo
        >>> a = AlbumFigs(300)
        >>> a.add_fig(4)
        >>> a.add_fig(4)
        >>> a.add_fig(4)
        >>> a.add_fig(7)
        >>> a.add_fig(7)
        >>> a.add_fig(1)
        >>> a.add_fig(1)
        >>> a.add_fig(1)
        >>> b = AlbumFigs(300)
        >>> b.add_fig(9)
        >>> b.add_fig(9)
        >>> b.add_fig(9)
        >>> b.add_fig(7)
        >>> b.add_fig(7)
        >>> b.add_fig(6)
        >>> b.add_fig(6)
        >>> b.add_fig(10)
        >>> b.add_fig(4)
        >>> b.add_fig(4)
        >>> # Cartinhas antes da troca
        >>> a.show()
        '[1, 4, 7]'
        >>> a.show_rep()
        '[1 (2), 4 (2), 7 (1)]'
        >>> b.show()
        '[4, 6, 7, 9, 10]'
        >>> b.show_rep()
        '[4 (1), 6 (1), 7 (1), 9 (2)]'
        >>> a.trocas_maximas(b)
        >>> # Cartinhas depois das trocas
        >>> a.show()
        '[1, 4, 6, 7]'
        >>> a.show_rep()
        '[1 (1), 4 (2), 7 (1)]'
        >>> b.show()
        '[1, 4, 6, 7, 9, 10]'
        >>> b.show_rep()
        '[4 (1), 7 (1), 9 (2)]'
        >>> # Não tem como trocar mais cartas, não faz nada
        >>> a.trocas_maximas(b)
        >>> a.show()
        '[1, 4, 6, 7]'
        >>> b.show()
        '[1, 4, 6, 7, 9, 10]'
        '''
        repetidas_a = self.verifica_nao_repetidas(b)
        repetidas_b = b.verifica_nao_repetidas(self)
        p = repetidas_a.inicio
        q = repetidas_b.inicio

        while p is not None and q is not None:
            self.add_fig(q.item)
            b.add_fig(p.item)
            self.rm_fig(p.item)
            b.rm_fig(q.item)
            p = p.prox
            q = q.prox
                

    def verifica_nao_repetidas(self, b: AlbumFigs) -> Fila:
        '''
        Cria uma lista com todas as figurinhas não repetidas de *self* e *b*
        Exemplos
        >>> a = AlbumFigs(300)
        >>> b = AlbumFigs(300)
        >>> a.add_fig(1)
        >>> a.add_fig(1)
        >>> a.add_fig(3)
        >>> a.add_fig(3)
        >>> a.add_fig(3)
        >>> a.add_fig(4)
        >>> a.add_fig(10)
        >>> a.add_fig(10)
        >>> b.add_fig(3)
        >>> b.add_fig(3)
        >>> b.add_fig(2)
        >>> b.add_fig(2)
        >>> b.add_fig(12)
        >>> b.add_fig(12)
        >>> b.add_fig(15)
        >>> b.add_fig(15)
        >>> a.show_rep()
        '[1 (1), 3 (2), 10 (1)]'
        >>> b.show_rep()
        '[2 (1), 3 (1), 12 (1), 15 (1)]'
        >>> a.verifica_nao_repetidas(b).show_f()
        '[1, 10]'
        >>> b.verifica_nao_repetidas(a).show_f()
        '[2, 12, 15]'
        '''
        naorepetidas = Fila()
        p = self.inicio
        q = b.inicio
        while p is not None:
            while q is not None and q.item.numero < p.item.numero:
                    q = q.prox
            if (q is None or q.item.numero > p.item.numero) and p.item.quantia > 1:
                naorepetidas.enfileira(p.item.numero)
            p = p.prox                
        return naorepetidas

    def vazio(self) -> bool:
        return self.fim is None
    