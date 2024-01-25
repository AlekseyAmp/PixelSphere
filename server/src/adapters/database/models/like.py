import pytz
from datetime import datetime

from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from src.adapters.database.models import Base
from src.adapters.database.settings import settings


class Like(Base):
    __tablename__ = "likes"
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    created_at = Column(DateTime(timezone=True), default=datetime.now(pytz.timezone(settings.TIMEZONE)))
    
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="likes")

    photo_id = Column(Integer, ForeignKey("photos.id", ondelete="CASCADE"))
    photo = relationship("Photo", back_populates="likes")
