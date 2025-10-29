from fila_modificada import Fila

def num_itens(f: Fila) -> int:
    '''
    Conta a quantidade de elementos de *f*.

    A fila *f* permanece com os mesmos itens e na mesma ordem.

    O tempo de execução da função é O(n^2). Fica como exercício fazer uma
    implementação com tempo de execução O(n).

    Exemplos
    >>> f = Fila(10)
    >>> num_itens(f)
    0
    >>> f.enfileira('a')
    >>> f.enfileira('b')
    >>> f.enfileira('a')
    >>> f.enfileira('b')
    >>> num_itens(f)
    4
    >>> # confirma que f não foi modificada
    >>> f.desenfileira()
    'a'
    >>> f.desenfileira()
    'b'
    >>> f.desenfileira()
    'a'
    >>> f.desenfileira()
    'b'
    '''
    if f.vazia():
        return 0
    else:
        primeiro = f.desenfileira()
        # Chama a função recursiva para determinar o número de itens sem o
        # primeiro e soma mais 1 relativo ao primeiro da fila
        num = num_itens(f) + 1
        # Agora precisamos voltar o primeiro, para isso, adiciona o primeiro no
        # fim da fila e "giramos" a fila até que o primeiro volte para o início
        # da fila
        f.enfileira(primeiro)
        for _ in range(num - 1):
            f.enfileira(f.desenfileira())
        return num
