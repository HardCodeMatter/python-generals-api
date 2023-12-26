from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from database import Base
from models.user import User


class Property(Base):
    __tablename__ = 'property'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    points: Mapped[int] = mapped_column(Integer, dafault=5)
    health: Mapped[int] = mapped_column(Integer, default=100)
    energy: Mapped[int] = mapped_column(Integer, default=100)
    ammunition: Mapped[int] = mapped_column(Integer, default=5)

    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'))
    user: Mapped['User'] = relationship(back_populates='property')
