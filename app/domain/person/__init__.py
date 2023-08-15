from app.domain.person import characteristics
from app.domain.person import dossier
from dataclasses import dataclass


@dataclass(kw_only=True)
class Person:
    ref: str
    characteristics: characteristics.Characteristics
    dossier: dossier.Dossier
