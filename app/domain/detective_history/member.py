from dataclasses import dataclass
from app.domain.person import Person
from app.domain.detective_history.status import PersonStatusInDetectiveHistory


@dataclass(kw_only=True)
class DetectiveHistoryMember:
    person: Person
    person_status: PersonStatusInDetectiveHistory = (
        PersonStatusInDetectiveHistory.INNOCENT
    )

    def __hash__(self) -> int:
        return hash(self.person.__hash__())
