from dataclasses import dataclass
from app.domain.detective_history.clue import Clue


@dataclass(kw_only=True)
class Proofs:
    ref: str
    description: str
    clues: set[Clue]

    def __hash__(self) -> int:
        return hash(self.ref)
