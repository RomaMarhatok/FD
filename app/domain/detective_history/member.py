from dataclasses import dataclass
import person
import status


@dataclass
class DetectiveHistoryMember:
    person: person.Person
    person_status: status.PersonStatusInDetectiveHistory = (
        status.PersonStatusInDetectiveHistory.INNOCENT
    )
