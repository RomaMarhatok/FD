import uuid
from dataclasses import dataclass, field


@dataclass
class Hobbies:
    description: str
    ref: uuid.UUID = field(default_factory=uuid.uuid4)
