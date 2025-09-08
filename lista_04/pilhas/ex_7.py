import ed
from pilha_arranjo import Pilha

def esvaziaPilha(pilha: Pilha):
    '''
    Retira todos os itens de uma pilha
    Exemplo
    >>> p = Pilha(5000000)
    >>> p.empilha('a')
    >>> p.empilha('a')
    >>> p.empilha('a')
    >>> p.vazia()
    False
    >>> esvaziaPilha(p)
    >>> p.vazia()
    True
    '''
    while not pilha.vazia():
        pilha.desempilha()

    # nova função seria so pilha.esvazia()

def invertePalavra(p: str) -> str:
    '''
    Inverte uma *p* usando uma pilha
    Exemplos
    >>> invertePalavra('abacate')
    'etacaba'
    '''
    pi = Pilha(len(p))
    for char in p:
        pi.empilha(char)
    arvalap = ''
    for char in p:
        arvalap += pi.desempilha()
    return arvalap

def removeVazios(p: Pilha):
    '''
    Remove os caracteres vazios ('') da pilha *p*
    Exemplos
    >>> p = Pilha(10)
    >>> p.empilha('a')
    >>> p.empilha('')
    >>> p.empilha('b')
    >>> p.empilha('')
    >>> p.empilha('')
    >>> p.empilha('')
    >>> removeVazios(p)
    >>> p.desempilha()
    'b'
    '''
    n = p.capacidade
    p_aux = Pilha(n)
    while not p.vazia():
        i = p.desempilha()
        if i != '':
            p_aux.empilha(i)
    while not p_aux.vazia():
        p.empilha(p_aux.desempilha())

def invertePilha(p: Pilha):
    '''
    Inverte a ordem dos itens de uma pilha
    Exemplos
    >>> p = Pilha(10)
    >>> p.empilha('a')
    >>> p.empilha('b')
    >>> p.empilha('c')
    >>> invertePilha(p)
    >>> p.desempilha()
    'a'
    '''
    n = p.capacidade
    p_aux = Pilha(n)
    p_aux2 = Pilha(n)
    while not p.vazia():
        p_aux.empilha(p.desempilha())
    while not p_aux.vazia():
        p_aux2.empilha(p_aux.desempilha())
    while not p_aux2.vazia():
        p.empilha(p_aux2.desempilha())