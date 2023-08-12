import uuid
import sex
import color
import special_sign
from dataclasses import field


class Characteristics:
    def __init__(
        self,
        weight: float,
        height: float,
        age: int,
        sex: sex.Sex,
        eyes: color.Color,
        hairs: color.Color,
        nationality: str,
        special_signs: list[special_sign.SpecialSign],
    ) -> None:
        self.id: uuid.UUID = field(default_factory=uuid.uuid4)
        self.weight = weight
        self.height = height
        self.age = age
        self.sex = sex
        self.eyes = eyes
        self.hairs = hairs
        self.special_signs = special_signs
        self.nationality = nationality
