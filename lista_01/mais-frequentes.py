from __future__ import annotations
from dataclasses import dataclass
from time import time
import sys


def main() -> None:
    if len(sys.argv) != 4:
        print(f'Modo de usar: python {sys.argv[0]} m n arquivo')
        print('  m - quantidade de palavras na saída')
        print('  n - quantidade de palavras para serem lidas do arquivo de entrada')
        sys.exit(1)

    m = int(sys.argv[1])

    n = int(sys.argv[2])

    palavras = list(open(sys.argv[3]).read().split())[:n]

    inicio = time()
    mais_frequentes = encontra_mais_frequentes(palavras, m)
    duracao = time() - inicio

    print('Palavras mais frequentes:')
    for c in mais_frequentes:
        print(c.palavra, c.vezes)

    print('Tempo de execução:', round(duracao, 2), 'segundos')


@dataclass
class PalavraVezes:
    '''
    Representa uma palavra e a quantidade de vezes que ela aparece em um corpus.
    '''
    palavra: str
    vezes: int

    def __lt__(self, outra: PalavraVezes) -> bool:
        '''
        Produz True se *self* aparece menos vezes que *outra* ou se aparece o
        mesmo número de vezes mas vem depois em ordem alfabética.
        Exemplos
        >>> PalavraVezes('casa', 3) < PalavraVezes('caso', 4)
        True
        >>> PalavraVezes('casa', 3) < PalavraVezes('caso', 3)
        False
        '''
        return self.vezes < outra.vezes or \
            self.vezes == outra.vezes and self.palavra > outra.palavra


def encontra_mais_frequentes(palavras: list[str], m: int) -> list[PalavraVezes]:
    '''
    Encontra as *m* palavras mais frequentes em *palavras*.
    Se a frequência de duas palavras for a mesma, então a
    que vem primeiro em ordem alfabética aparece primeiro.

    Se *m* for maior que a quantidade de palavras distintas,
    então devolve a frequência de todas as palavras.

    Requer que m > 0.

    Exemplos
    >>> encontra_mais_frequentes(['casa', 'de', 'a', 'ti', 'de', 'a', 'casa', 'a', 'de'], 3)
    [PalavraVezes(palavra='a', vezes=3), PalavraVezes(palavra='de', vezes=3), PalavraVezes(palavra='casa', vezes=2)]
    '''
    lista_palavrasvezes: list[PalavraVezes] = []
    for palavra in palavras:
        not_esta_lista = True
        i = 0
        while not_esta_lista and i < len(lista_palavrasvezes):
            if lista_palavrasvezes[i].palavra == palavra:
                lista_palavrasvezes[i].vezes += 1
                not_esta_lista = False
            i += 1
        if not_esta_lista:
            lista_palavrasvezes.append(PalavraVezes(palavra, 1))
    for i in range (len(lista_palavrasvezes)):
        for j in range (i+1, len(lista_palavrasvezes)):
            if lista_palavrasvezes[i] < lista_palavrasvezes[j]:
                troca(lista_palavrasvezes, i, j)
    return lista_palavrasvezes[:m]

def particiona(lst: list[PalavraVezes], ini: int, fim: int) -> int:
    pivo = lst[fim - 1]
    menores = []
    maiores_iguais = []
    for i in range(ini, fim - 1):
        if lst[i] < pivo:
            menores.append(lst[i])
        else:
            maiores_iguais.append(lst[i])
    # Copia os menores do que o pivo para lst
    for i in range(len(menores)):
        lst[i] = menores[i]
    # Copia o pivo para lst
    p = len(menores)
    lst[p] = pivo
    # Copias os maiores ou iguais ao pivo para lst
    for j in range(len(maiores_iguais)):
        lst[p + j + 1] = maiores_iguais[j]
    return p # Retorna o índice do pivo

def troca(lst: list, i: int, j: int) -> None:
    '''
    Move o elemento da posição *i* de *lst* para a posição *j* e vice-versa.

    Requer que *i* e *j* sejam posições valídas de *lst*.

    Exemplos
    >>> lst = [5, 1, 6, 8, 2]
    >>> troca(lst, 2, 4)
    >>> lst
    [5, 1, 2, 8, 6]
    '''
    lst[i], lst[j] = lst[j], lst[i]


if __name__ == "__main__":
    main()
