import enum


class CriminalType(str, enum.Enum):
    MARDER = "MARDER"
    MANIAC = "MANIAC"
    POISONER = "POISONER"
    STRANGLER = "STRANGLER"
    DISMANTLER = "DISMANTLER"
    THIEF = "THIEF"
