import uuid
from dataclasses import field
import member as history_member
import status
import clue
import proofs


class DetectiveHistory:
    clues: set[clue.Clue]
    proofs: set[proofs.Proofs]
    incident_description: str
    members: set[history_member.DetectiveHistoryMember]
    answer: history_member.DetectiveHistoryMember
    ref: uuid.UUID = field(default_factory=uuid.uuid4)

    @property
    def suspect(self) -> list[history_member.DetectiveHistoryMember]:
        return [
            member
            for member in self.members
            if member.person_status == status.PersonStatusInDetectiveHistory.SUSPECT
        ]

    @property
    def witnesses(self) -> list[history_member.DetectiveHistoryMember]:
        return [
            member
            for member in self.members
            if member.person_status == status.PersonStatusInDetectiveHistory.WITNESS
        ]

    @property
    def guilty(self) -> history_member.DetectiveHistoryMember | None:
        for member in self.members:
            if member.person_status == status.PersonStatusInDetectiveHistory.GUILTY:
                return member
        return None
