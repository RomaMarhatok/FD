import person
import status

# from . import DetectiveHistory


class DetectiveHistoryMember:
    # detective_history: DetectiveHistory
    person: person.Person
    person_status: status.PersonStatusInDetectiveHistory = (
        status.PersonStatusInDetectiveHistory.INNOCENT
    )
