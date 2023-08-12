import enum


class MarriageStatus(str, enum.Enum):
    MARRIED = "MARRIED"
    UNMARRIED = "UNMARRIED"
    DIVORCED = "DIVORCED"
