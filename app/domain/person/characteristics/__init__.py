from app.domain.person.characteristics import sex
from app.domain.person.characteristics import color
from app.domain.person.characteristics import special_sign
from dataclasses import dataclass


@dataclass(kw_only=True)
class Characteristics:
    ref: str
    weight: float
    height: float
    age: int
    sex: sex.Sex
    _eyes_color: color.Color
    _hairs_color: color.Color
    nationality: str
    special_signs: set[special_sign.SpecialSign]

    @property
    def eyes(self) -> color.Color:
        return self._eyes_color

    @property
    def hairs(self) -> color.Color:
        return self._hairs_color

    def __hash__(self) -> int:
        return hash(self.ref)
