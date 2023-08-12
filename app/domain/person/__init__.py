import uuid
import characteristics
import dossier
from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Person:
    id: uuid.UUID = field(default_factory=uuid.uuid4)
    characteristics: characteristics.Characteristics
    additional_information: dossier.Dossier
