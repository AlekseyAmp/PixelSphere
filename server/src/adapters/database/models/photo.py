import pytz
from datetime import datetime

from sqlalchemy import Column, Integer, String, LargeBinary, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from adapters.database.sa_session import Base
from adapters.database.settings import settings
from adapters.database.models.user import User


class Photo(Base):
    __tablename__ = "photos"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    title = Column(String)
    description = Column(String)
    image = Column(LargeBinary)
    created_at = Column(DateTime(timezone=True), default=datetime.now(pytz.timezone(settings.TIMEZONE)))
    
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship(User, back_populates="photos")

    likes = relationship("Like", back_populates="photo")
    comments = relationship("Comment", back_populates="photo")
