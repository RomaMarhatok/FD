from dataclasses import dataclass
import clue


@dataclass
class Proofs:
    clue: clue.Clue
    description: str
