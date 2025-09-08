class BancoHoras:
    '''
    Cria um banco de horas com horas e minutos que devem seguir o padrão HH:MM, 
    que pode variar, mas sempre manter o padrão de maximo 60 min e não podem ser
    negativas. 
    '''
    horas: int
    minutos:int

    def __init__ (self) -> None:
        '''
        Cria um banco de horas que começa em 0 horas e 0 minutos
        Exemplos
        >>> b = BancoHoras()
        >>> b.checarHoras()
        '00:00'
        '''
        self.horas = 0
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
        self.horas += h
        self.minutos += m
        self.corrigeHoras()

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
        c = BancoHoras()
        c.minutos = m
        c.horas = h
        c.corrigeHoras()
        if self.horas < c.horas or self.horas == c.horas and self.minutos < c.minutos:
            print('Não possui saldo suficiente para remover essas horas')
        else:
            self.horas -= h
            self.minutos -= m
        self.corrigeHoras()

    def corrigeHoras (self):
        '''
        Corrige as horas caso os *self.minutos* >= 60
        Exemplos
        >>> b = BancoHoras()
        >>> b.adicionaHorasMinutos(0, 59)
        >>> b.checarHoras()
        '00:59'
        >>> b.adicionaHorasMinutos(0, 1)
        >>> b.checarHoras()
        '01:00'
        >>> b.removeHorasMinutos(0, 1)
        >>> b.checarHoras()
        '00:59'
        '''
        self.horas += self.minutos // 60
        self.minutos = self.minutos % 60

    
    def checarHoras(self) -> str:
        '''
        Retorna as horas e minutos no formato 'HH:MM'
        '''
        h = str(self.horas)
        m = str(self.minutos)
        if len(h) < 2:
            HH = '0' + h
        if len(h) >= 2:
            HH = h
        if len(m) < 2:
            MM = '0' + m
        if len(m) == 2:
            MM = m
        return HH + ':' + MM