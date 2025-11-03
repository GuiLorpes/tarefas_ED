from __future__ import annotations
from ed import array
from dataclasses import dataclass


CAPACIDADE_INICIAL = 4
FATOR_CRESCIMENTO = 2.0


@dataclass
class Figurinha:
    '''
    Uma figurinha e a sua quantidade.
    '''
    numero: int
    quantidade: int


class Lista:
    '''
    Um arranjo dinâmico de figurinhas.
    '''
    valores: array[Figurinha]
    tamanho: int


    def __init__(self) -> None:
        self.valores = array(CAPACIDADE_INICIAL, Figurinha(0, 0))
        self.tamanho = 0

    def __cresce(self):
        '''
        Aloca os elementos de *self* em um arranjo *FATOR_CRESCIMENTO* vezes maior que *self.valores*.
        '''
        nova_capacidade = int(len(self.valores) * FATOR_CRESCIMENTO)
        novo_array = array(nova_capacidade, Figurinha(0, 0))

        for i in range(len(self.valores)):
            novo_array[i] = self.valores[i]

        self.valores = novo_array

    def __diminui(self):
        '''
        Aloca os elementos de *self* em um arranjo *FATOR_CRESCIMENTO* vezes menor que *self.valores*.
        '''
        nova_capacidade = int(len(self.valores) * FATOR_CRESCIMENTO)
        novo_array = array(nova_capacidade, Figurinha(0, 0))

        for i in range(len(self.valores)):
            novo_array[i] = self.valores[i]

        self.valores = novo_array

    def num_itens(self) -> int:
        '''
        Retorna a quantidade de itens no arranjo.

        Exemplo:
        >>> a = Lista()
        >>> a.insere_ordenado(Figurinha(1,1))
        >>> a.insere_ordenado(Figurinha(2,1))
        >>> a.num_itens()
        2
        >>> a.remove(0)
        >>> a.num_itens()
        1
        >>> a.insere_ordenado(Figurinha(3,1))
        >>> a.num_itens()
        2
        '''
        return self.tamanho

    def insere_ordenado(self, fig: Figurinha):
        '''
        Insere *fig* de forma ordenada em *self.valores*.
        Os elementos que estavam nas posições i, i+1, i+2... ocuparão as posições i+1, i+2, i+3...
        Requer que 0 <= i <= self.num_itens().

        Exemplo:
        >>> a = Lista()
        >>> a.insere_ordenado(Figurinha(3,1))
        >>> a.insere_ordenado(Figurinha(5,1))
        >>> a.insere_ordenado(Figurinha(4,1))
        >>> a.str()
        '[(3, 1), (4, 1), (5, 1)]'
        '''
        if self.tamanho == len(self.valores) - 1:
            self.__cresce()

        encontrado = False
        i = 0
        while i < self.tamanho and not encontrado:
            if fig.numero < self.valores[i].numero:
                encontrado = True
            else:
                i += 1

        for j in range(self.tamanho, i, -1):
             self.valores[j] = self.valores[j-1]

        self.valores[i] = fig
        self.tamanho += 1

    def remove(self, i: int):
        '''
        Remove o elemento na posição *i* de *self*.
        Os elementos que estavam nas posições i+1, i+2, i+3... ocuparão as posições i, i+1, i+2...
        Requer que 0 <= i < self.num_itens().

        Exemplo:
        >>> a = Lista()
        >>> a.insere_ordenado(Figurinha(6,1))
        >>> a.insere_ordenado(Figurinha(8,1))
        >>> a.str()
        '[(6, 1), (8, 1)]'
        >>> a.remove(0)
        >>> a.str()
        '[(8, 1)]'
        '''
        if i < 0 or i >= self.tamanho:
            raise ValueError('Índice fora da faixa')
        
        if self.tamanho - 1 < len(self.valores) / 4:
            self.__diminui()

        for j in range(i, self.tamanho):
            self.valores[j] = self.valores[j+1]
        self.tamanho -= 1
    
    def get(self, i: int) -> Figurinha:
        '''
        Retorna o item de *self* na posição *i*.
        Requer que 0 <= i < self.num_itens()

        Exemplo:
        >>> a = Lista()
        >>> a.insere_ordenado(Figurinha(5,1))
        >>> a.get(0)
        Figurinha(numero=5, quantidade=1)
        '''
        if i < 0 or i >= self.tamanho:
            raise ValueError('Índice fora da faixa')
        
        item = self.valores[i]
        assert item is not None

        return item

    def indice(self, fig: int) -> int | None:
        '''
        Retorna o índice de *fig* em *self* e None se *fig* não existir em *self.

        Exemplo:
        >>> a = Lista()
        >>> a.insere_ordenado(Figurinha(2,1))
        >>> a.indice(4)
        >>> a.indice(2)
        0
        '''
        resposta: int | None = None

        for i in range(self.num_itens()):
            if self.valores[i].numero == fig:
                resposta = i
        
        return resposta
    
    def repetidas(self) -> Lista:
        '''
        Retorna uma Lista com as figurinhas repetidas de *self.valores*.

        Exemplo:
        >>> a = Lista()
        >>> a.insere_ordenado(Figurinha(2,4))
        >>> a.insere_ordenado(Figurinha(3,2))
        >>> a.insere_ordenado(Figurinha(4,1))
        >>> rep = a.repetidas()
        >>> rep.str()
        '[(2, 3), (3, 1)]'
        '''
        rep = Lista()

        for i in range (self.tamanho):
            if self.get(i).quantidade > 1:
                rep.insere_ordenado(Figurinha(self.get(i).numero, self.get(i).quantidade - 1))

        return rep
    
    def diferenca(self, lst: Lista) -> Lista:
        '''
        Retorna uma arranjo estático com os elementos de *self* que não estão em *lst*.

        Exemplo:
        >>> a = Lista()
        >>> a.insere_ordenado(Figurinha(2,1))
        >>> a.insere_ordenado(Figurinha(3,2))
        >>> a.insere_ordenado(Figurinha(4,3))
        >>> b = Lista()
        >>> b.insere_ordenado(Figurinha(3,1))
        >>> b.insere_ordenado(Figurinha(5,4))
        >>> dif = a.diferenca(b)
        >>> dif.str()
        '[(2, 1), (4, 1)]'
        '''
        resposta = Lista()

        for i in range(self.tamanho):
            n_fig = self.valores[i].numero

            if lst.indice(n_fig) is None:
                resposta.insere_ordenado(Figurinha(n_fig, 1))
        
        return resposta
    
    def str(self) -> str:
        '''
        Cria uma string com os elementos de *self*.

        Exemplo:
        >>> a = Lista()
        >>> a.str()
        '[]'
        >>> a.insere_ordenado(Figurinha(2, 1))
        >>> a.insere_ordenado(Figurinha(4, 1))
        >>> a.str()
        '[(2, 1), (4, 1)]'
        '''
        string = '['
        if self.tamanho != 0:
            texto = self.valores[0]
            assert texto is not None
            string += '(' + str(texto.numero) + ', ' + str(texto.quantidade) + ')'

            for i in range(1, self.tamanho):
                texto = self.valores[i]
                assert texto is not None
                string += ', (' + str(texto.numero) + ', ' + str(texto.quantidade) + ')'

        return string + ']'
    
class AlbumFigs:
    ''' 
    Um álbum de figurinhas onde cada figurinha é um inteiro positivo.
    Exemplos
    >>> a = AlbumFigs(300)
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
    >>> a.rm_fig(45)
    >>> a.rm_fig(500)
    >>> a.show()
    '[1, 3]'
    >>> a.show_rep()
    '[3 (1)]'
    '''
    figs_diferentes: int
    figs: Lista

    def __init__(self, c: int):
        ''' 
        Cria um novo álbum com *c* figurinhas diferentes.
        '''
        self.figs_diferentes = c
        self.figs = Lista()

    def __no_intervalo(self, fig: int) -> bool:
        '''
        Retorna True se *fig* é uma das figurinhas possíveis de *self*.
        '''
        return fig > 0 and fig <= self.figs_diferentes

    def add_fig(self, fig:int):
        '''
        Se *fig* estiver no álbum, a quantidade dela é aumentada em 1.
        Caso contrário, *fig* é adicionada ao álbum com quantidade 1.
        Nada acontece se *fig* não estiver no intervalo de figurinhas possíveis do álbum.
        '''
        if self.__no_intervalo(fig):
            indice_em_figs = self.figs.indice(fig)

            if indice_em_figs is None:
                self.figs.insere_ordenado(Figurinha(fig, 1))
            
            else:
                self.figs.get(indice_em_figs).quantidade += 1
            
    def rm_fig(self, fig:int):
        '''
        Se *fig* estiver no álbum, a quantidade dela é diminuida em 1 e, caso sua quantidade chegue
        a zero, ela é removida do álbum.
        Caso contrário, nada acontece.
        Nada acontece se *fig* não estiver no intervalo de figurinhas possíveis do álbum.
        '''
        if self.__no_intervalo(fig):
            indice_em_figs = self.figs.indice(fig)

            if indice_em_figs is not None:
                figurinha = self.figs.get(indice_em_figs)
                
                if figurinha.quantidade > 1:
                    figurinha.quantidade -= 1
            
                else:
                    self.figs.remove(indice_em_figs)
                    
    def show(self) -> str:
        '''
        Mostra todos as figurinhas do album sem mostrar as quantias de cada
        '''
        resposta = '['

        if self.figs.tamanho > 0:
            resposta += str(self.figs.get(0).numero)

            for i in range(1, self.figs.tamanho):
                resposta += ', ' + str(self.figs.get(i).numero)

        return resposta + ']'

    def show_rep(self) -> str:
        '''
        Mostra todas as figurinhas repetidas e sua quantidade
        '''
        repetidas = self.figs.repetidas()
        resposta = '['

        if repetidas.tamanho > 0:
            resposta += str(repetidas.get(0).numero) + ' (' + str(repetidas.get(0).quantidade) + ')'

            for i in range(1, repetidas.tamanho):
                resposta += ', ' + str(repetidas.get(i).numero) + ' (' + str(repetidas.get(i).quantidade) + ')'

        return resposta + ']'

    def trocas_maximas(self, alb: AlbumFigs):
        '''
        Verifica quantas cartas de *self* é possivel trocar com *alb*, e troca em
        pares as cartinhas dos dois albuns, caso não seja possivel realizar 
        nenhuma troca, não faz nada.
        
        Exemplo:
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
        self_pode_receber = alb.figs.repetidas().diferenca(self.figs)
        alb_pode_receber = self.figs.repetidas().diferenca(alb.figs)

        while self_pode_receber.tamanho > 0 and alb_pode_receber.tamanho > 0:
            self.add_fig(self_pode_receber.get(0).numero)
            alb.rm_fig(self_pode_receber.get(0).numero)
            self_pode_receber.remove(0)

            alb.add_fig(alb_pode_receber.get(0).numero)
            self.rm_fig(alb_pode_receber.get(0).numero)
            alb_pode_receber.remove(0)
