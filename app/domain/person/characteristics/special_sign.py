from dataclasses import dataclass


@dataclass(kw_only=True)
class SpecialSign:
    ref: str
    description: str
