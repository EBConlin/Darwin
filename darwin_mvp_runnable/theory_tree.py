from dataclasses import dataclass, field
from typing import List, Union, Dict
import random

@dataclass(frozen=True)
class TheoryNode:
    op: str
    args: List[Union['TheoryNode', str, float]]
    metadata: Dict = field(default_factory=dict)

def generate_random_theory(depth=2):
    ops = ['+', '-', '*', '/', 'log']
    variables = ['x', 'y', 1, 2, 3, 0.5]

    if depth == 0:
        return random.choice(variables)
    else:
        op = random.choice(ops)
        arg1 = generate_random_theory(depth - 1)
        arg2 = generate_random_theory(depth - 1)
        return TheoryNode(op=op, args=[arg1, arg2])