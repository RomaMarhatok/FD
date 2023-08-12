import enum


class PersonStatusInDetectiveHistory(str, enum.Enum):
    SUSPECT = "SUSPECT"
    WITNESS = "WITNESS"
    CRIMINAL = "CRIMINAL"
    INNOCENT = "INNOCENT"
    GUILTY = "GUILTY"
