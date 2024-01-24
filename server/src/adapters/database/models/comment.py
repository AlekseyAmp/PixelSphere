import pytz
from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from adapters.database.sa_session import Base
from adapters.database.settings import settings


class Comment(Base):
    __tablename__ = "comments"
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    text = Column(String)
    created_at = Column(DateTime(timezone=True), default=datetime.now(pytz.timezone(settings.TIMEZONE)))
    
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="comments")

    photo_id = Column(Integer, ForeignKey("photos.id", ondelete="CASCADE"))
    photo = relationship("Photo", back_populates="comments")
