from sqlalchemy import Column, Integer, String, DateTime, func
from app.base.model import Base


# Модель пользователя
class LinkModel(Base):
    __tablename__ = 'links'
    id = Column(Integer, primary_key=True)
    short = Column(String, unique=True, nullable=False)
    full = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False, default=func.now())
