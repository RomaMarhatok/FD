from sqlalchemy.orm import registry
from app.db.models.person.special_sign import special_sing_model
from app.domain.person.characteristics.special_sign import SpecialSign


def init_mappers():
    mapper = registry()
    mapper.map_imperatively(SpecialSign, special_sing_model)


init_mappers()
