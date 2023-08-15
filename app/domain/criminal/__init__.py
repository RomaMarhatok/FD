from app.domain.person import Person
from app.domain.criminal.criminal_type import CriminalType
from dataclasses import dataclass


@dataclass
class Criminal:
    person: Person
    criminal_type: CriminalType
