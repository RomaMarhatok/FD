import hobbies
import motives
from status import marrige_status, social_status


class Dossier:
    def __init__(
        self,
        history: str,
        hobbies: list[hobbies.Hobbies],
        motives: list[motives.Motives],
        social_status: social_status.SocialStatus,
        marriage_status: marrige_status.MarriageStatus,
    ) -> None:
        self.history = history
        self.hobbies = hobbies
        self.motives = motives
        self.social_status = social_status
        self.marriage_status = marriage_status
