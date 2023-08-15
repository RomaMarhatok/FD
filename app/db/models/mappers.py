from sqlalchemy.orm import registry, relationship, composite
from app.db.models.person.special_sign import special_sing_table
from app.db.models.person.motives import motives_table
from app.db.models.person.hobbies import hobbies_table
from app.db.models.person.characteristics import (
    characteristics_table,
    special_sign_in_characteristics_table,
)
from app.db.models.person.dossier import (
    dossier_table,
    dossier_motives_table,
    dossier_hobbies_table,
)
from app.db.models.person.person import person_table
from app.domain.person.characteristics.special_sign import SpecialSign
from app.domain.person.characteristics import Characteristics, color
from app.domain.person.dossier.motives import Motives
from app.domain.person.dossier.hobbies import Hobbies
from app.domain.person.dossier import Dossier
from app.domain.person import Person


def init_mappers():
    mapper = registry()
    special_sing_mapper = mapper.map_imperatively(
        SpecialSign,
        special_sing_table,
    )
    characteristics_mapper = mapper.map_imperatively(
        Characteristics,
        characteristics_table,
        properties={
            "_eyes_color": composite(
                lambda value: color.Color.color_from_name(value),
                characteristics_table.c.eyes_color,
            ),
            "_hairs_color": composite(
                lambda value: color.Color.color_from_name(value),
                characteristics_table.c.hairs_color,
            ),
            "special_signs": relationship(
                special_sing_mapper,
                secondary=special_sign_in_characteristics_table,
                collection_class=set,
            ),
        },
    )
    motive_mapper = mapper.map_imperatively(Motives, motives_table)
    hobby_mapper = mapper.map_imperatively(Hobbies, hobbies_table)
    dossier_mapper = mapper.map_imperatively(
        Dossier,
        dossier_table,
        properties={
            "hobbies": relationship(
                hobby_mapper,
                secondary=dossier_hobbies_table,
                collection_class=set,
            ),
            "motives": relationship(
                motive_mapper,
                secondary=dossier_motives_table,
                collection_class=set,
            ),
        },
    )
    mapper.map_imperatively(
        Person,
        person_table,
        properties={
            "characteristics": relationship(
                characteristics_mapper,
            ),
            "dossier": relationship(
                dossier_mapper,
            ),
        },
    )
