import pytz
from datetime import datetime

from sqlalchemy import Column, Integer, String, LargeBinary, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from src.adapters.database.models import Base
from src.adapters.database.settings import settings


class Photo(Base):
    __tablename__ = "photos"
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    title = Column(String)
    description = Column(String)
    image = Column(LargeBinary)
    created_at = Column(DateTime(timezone=True), default=datetime.now(pytz.timezone(settings.TIMEZONE)))    
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="photos")

    likes = relationship(
        "Like",
        back_populates="photo",
        cascade="all, delete",
        passive_deletes=True,
    )
    comments = relationship(
        "Comment",
        back_populates="photo",
        cascade="all, delete",
        passive_deletes=True,
    )
