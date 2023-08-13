import uuid
from dataclasses import field


class Clue:
    description: str
    ref: uuid.UUID = field(default_factory=uuid.uuid4)
