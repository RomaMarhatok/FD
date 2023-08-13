import uuid
from dataclasses import dataclass, field


@dataclass
class Motives:
    description: str
    ref: uuid.UUID = field(default_factory=uuid.uuid4)
