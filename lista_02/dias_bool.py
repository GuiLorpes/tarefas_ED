from enum import Enum


class Dia(Enum):
    '''
    Um dia da semana.
    '''
    DOM = 0
    SEG = 1
    TER = 2
    QUA = 3
    QUI = 4
    SEX = 5
    SAB = 6


class Dias:
    '''
    Um conjunto de dias da semana que um evento deve se repetir.
    '''
    evento: list[Dia]

    def __init__(self) -> None:
        '''
        Cria um novo conjunto vazio de dias.

        Exemplos
        >>> c = Dias()
        >>> c.lista()
        []
        '''
        self.evento = []

    def alterna(self, d: Dia):
        '''
        Alterna a pertinencia do dia *d* em *self*, isto é, se *d* está em
        *self*, *d* é removido. Se *d* não está em *self*, *d* é adicionado.

        Exemplos
        >>> c = Dias()
        >>> c.alterna(Dia.SEX)
        >>> c.lista()
        ['sex']
        >>> c.alterna(Dia.SEG)
        >>> c.lista()
        ['seg', 'sex']
        >>> c.alterna(Dia.SEX)
        >>> c.lista()
        ['seg']
        '''
        i = 0 
        ja_tem = False
        while i < len(self.evento) and not ja_tem:
            ja_tem = d == self.evento[i]
            i += 1
        if ja_tem:
            self.evento = self.evento[:i-1] + self.evento[i:]
        else:
            self.evento.append(d)


    def lista(self) -> list[str]:
        '''
        Devolve uma lista com os dias (abreviações) em ordem da semana que
        estão em *self*.

        Exemplos
        >>> c = Dias()
        >>> c.lista()
        []
        >>> c.alterna(Dia.TER)
        >>> c.lista()
        ['ter']
        >>> c.alterna(Dia.DOM)
        >>> c.lista()
        ['dom', 'ter']
        >>> c.alterna(Dia.QUI)
        >>> c.alterna(Dia.SEG)
        >>> c.alterna(Dia.SAB)
        >>> c.alterna(Dia.QUA)
        >>> c.alterna(Dia.SEX)
        >>> c.lista()
        ['dom', 'seg', 'ter', 'qua', 'qui', 'sex', 'sab']
        '''
        lista_self = []
        lista_atualizada = []
        for i in range (len(self.evento)):
            lista_self.append(self.evento[i])
        for i in range (len(lista_self)):
            for j in range (i+1, len(lista_self)):
                if lista_self[i].value > lista_self[j].value:
                    lista_self[i], lista_self[j] = lista_self[j], lista_self[i]
        for dia in lista_self:
            lista_atualizada.append(str(dia.name).lower())
        return lista_atualizada