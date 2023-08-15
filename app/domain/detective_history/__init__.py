from dataclasses import dataclass
from app.domain.person import Person
from app.domain.detective_history import status, clue, proofs, member as history_member


@dataclass(kw_only=True)
class DetectiveHistory:
    ref: str
    clues: set[clue.Clue]
    proofs: set[proofs.Proofs]
    incident_description: str
    members: set[history_member.DetectiveHistoryMember]
    history_answer: Person

    def _get_members(
        self, member_status: status.PersonStatusInDetectiveHistory
    ) -> list[history_member.DetectiveHistoryMember]:
        return [
            member for member in self.members if member.person_status == member_status
        ]

    @property
    def suspect(self) -> list[history_member.DetectiveHistoryMember]:
        return self._get_members(status.PersonStatusInDetectiveHistory.SUSPECT)

    @property
    def witnesses(self) -> list[history_member.DetectiveHistoryMember]:
        return self._get_members(status.PersonStatusInDetectiveHistory.WITNESS)

    @property
    def guilty(self) -> history_member.DetectiveHistoryMember | None:
        for member in self.members:
            if member.person_status == status.PersonStatusInDetectiveHistory.GUILTY:
                return member
        return None
