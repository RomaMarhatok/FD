from dataclasses import dataclass
from app.domain.person.dossier import hobbies
from app.domain.person.dossier import motives
from app.domain.person.dossier.status import marrige_status, social_status


@dataclass
class Dossier:
    ref: str
    history: str
    hobbies: set[hobbies.Hobbies]
    motives: set[motives.Motives]
    social_status: social_status.SocialStatus
    marriage_status: marrige_status.MarriageStatus
