from app.db.models.person.special_sign import special_sing_table
from app.db.models.person.hobbies import hobbies_table
from app.db.models.person.characteristics import (
    characteristics_table,
    special_sign_in_characteristics_table,
)
from app.db.models.mappers import init_mappers

init_mappers()
