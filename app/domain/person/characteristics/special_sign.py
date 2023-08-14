from dataclasses import dataclass


@dataclass(kw_only=True)
class SpecialSign:
    ref: str
    description: str

    def __hash__(self) -> int:
        return hash(self.ref)
