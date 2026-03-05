# models.py - SQLAlchemy models for URL shortening service

from sqlalchemy import Column, Integer, String,Text,DateTime
from sqlalchemy.sql import func
from .database import Base

# URL model representing the urls table in the database
# (Base) -> inherits from the declarative base defined in database.py
# id: primary key, auto-incrementing integer
# long_url: the original long URL, cannot be null
# short_code: the generated short code for the URL, unique and indexed, can be null
# created_at: timestamp of when the URL was created, defaults to the current time
class URL(Base):
    __tablename__ = "urls"
    id = Column(Integer, primary_key=True, index=True)
    long_url = Column(Text, nullable=False)
    short_code = Column(String(10), unique=True, index=True, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())