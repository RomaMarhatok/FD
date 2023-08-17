from app.domain.person import Person
from app.domain.person.characteristics import Characteristics, color, sex
from app.domain.person.dossier import Dossier
from app.domain.person.dossier.status.social_status import SocialStatus
from app.domain.person.dossier.status.marrige_status import MarriageStatus
from app.domain.detective_history import DetectiveHistory
from app.domain.detective_history.clue import Clue
from app.domain.detective_history.proofs import Proofs
from app.domain.detective_history.member import DetectiveHistoryMember


async def make_person() -> Person:
    characteristics = Characteristics(
        ref="characteristics-ref",
        weight=12.3,
        height=10.3,
        age=10,
        sex=sex.Sex.MALE,
        _eyes_color=color.Color.color_from_name("blue"),
        _hairs_color=color.Color.color_from_name("brown"),
        nationality="chinese",
        special_signs=set(),
    )

    dossier = Dossier(
        "dossier-ref",
        "some history text 1",
        set(),
        set(),
        SocialStatus.WORKS,
        MarriageStatus.MARRIED,
    )

    person = Person(
        ref="person-ref",
        characteristics=characteristics,
        dossier=dossier,
    )
    return person


async def make_detective_history() -> DetectiveHistory:
    clue = Clue(ref="ref-1", description="clue description")
    proof = Proofs(ref="proof-ref", description="proof descirption", clues={clue})
    person = await make_person()
    member = DetectiveHistoryMember(person=person)
    return DetectiveHistory(
        ref="detective_history_ref",
        incident_description="incident description",
        clues={clue},
        proofs={proof},
        members={member},
        history_answer=person,
    )
