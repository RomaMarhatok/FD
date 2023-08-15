from dataclasses import dataclass


@dataclass(kw_only=True)
class Clue:
    ref: str
    description: str
