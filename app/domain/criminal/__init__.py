import person
import criminal_type
from dataclasses import dataclass


@dataclass
class Criminal:
    person: person.Person
    criminal_type: criminal_type.CriminalType
