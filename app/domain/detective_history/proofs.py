import uuid
from dataclasses import dataclass, field
import clue


@dataclass
class Proofs:
    clue: clue.Clue
    description: str
    ref: uuid.UUID = field(default_factory=uuid.uuid4)
