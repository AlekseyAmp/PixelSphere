import pytz
from datetime import datetime

from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from adapters.database.sa_session import Base
from adapters.database.settings import settings
from adapters.database.models.user import User
from adapters.database.models.photo import Photo


class Like(Base):
    __tablename__ = "likes"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    created_at = Column(DateTime(timezone=True), default=datetime.now(pytz.timezone(settings.TIMEZONE)))
    
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship(User, back_populates="likes")

    photo_id = Column(Integer, ForeignKey("photos.id"))
    photo = relationship(Photo, back_populates="likes")
