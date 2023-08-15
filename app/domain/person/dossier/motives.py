from dataclasses import dataclass


@dataclass
class Motives:
    ref: str
    description: str

    def __hash__(self) -> int:
        return hash(self.ref)
