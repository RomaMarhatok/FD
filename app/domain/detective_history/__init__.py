import member as history_member
import status


class DetectiveHistory:
    clues: list[str]  # rework
    proofs: list[str]  # rework
    incident_description: str
    members: list[history_member.DetectiveHistoryMember]
    answer: history_member.DetectiveHistoryMember

    @property
    def suspect(self) -> list:
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
