from __future__ import annotations
from dataclasses import dataclass

@dataclass
class Node:
    ''' Um nó de inteiros '''
    item: int
    prox: Node | None

p = Node(7, None)
p.prox = Node(1, None)
p.prox.prox = Node(2, None)

def transforma_list_em_no(lst: list) -> Node:
    