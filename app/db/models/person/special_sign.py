from sqlalchemy import Column, Text, UUID
from app.db.models.base import SqlAlchemyBaseModel


class SpecialSignModel(SqlAlchemyBaseModel):
    __tablename__ = "special_sign"
    id = Column(UUID(as_uuid=True), primary_key=True)
    ref = Column(UUID(as_uuid=True), unique=True, nullable=True)
    description = Column(Text())
