class BancoHoras:
    '''
    Cria um banco de horas com horas e minutos que devem seguir o padrão HH:MM, 
    que pode variar, mas sempre manter o padrão de maximo 60 min e não podem ser
    negativas. 
    '''
    minutos: int

    def __init__ (self) -> None:
        '''
        Cria um banco de horas que começa em 0 horas e 0 minutos
        Exemplos
        >>> b = BancoHoras()
        >>> b.checarHoras()
        '00:00'
        '''
        self.minutos = 0

    def adicionaHorasMinutos (self, h: int, m: int):
        '''
        Adiciona *h* ou *m* ao banco de horas
        Exemplos
        >>> b = BancoHoras()
        >>> b.adicionaHorasMinutos(5, 0)
        >>> b.checarHoras()
        '05:00'
        >>> b.adicionaHorasMinutos(0, 90)
        >>> b.checarHoras()
        '06:30'
        '''
        self.minutos += (h * 60) + m

    def removeHorasMinutos (self, h: int, m: int):
        '''
        Remove *h* ou *m* do banco de horas, caso o valor a retirar 
        seja maior que o do banco, não faça nada.
        Exemplos
        >>> b = BancoHoras()
        >>> b.adicionaHorasMinutos(2, 45)
        >>> b.checarHoras()
        '02:45'
        >>> b.removeHorasMinutos(3, 0)
        Não possui saldo suficiente para remover essas horas
        >>> b.checarHoras()
        '02:45'
        >>> b.removeHorasMinutos(2, 10)
        >>> b.checarHoras()
        '00:35'
        '''
        if self.minutos < (h * 60) + m:
            print('Não possui saldo suficiente para remover essas horas')
        else:
            self.minutos -= (h * 60) + m

    def checarHoras(self) -> str:
        '''
        Retorna as horas e minutos no formato 'HH:MM'
        '''
        h = str((self.minutos) // 60)
        m = str((self.minutos) % 60)
        if len(h) < 2:
            HH = '0' + h
        if len(h) >= 2:
            HH = h
        if len(m) < 2:
            MM = '0' + m
        if len(m) == 2:
            MM = m
        return HH + ':' + MM
        