from sqlalchemy import Column, Integer, String, Float, CheckConstraint
from app.database import Base

class Movie(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    genre = Column(String, index=True)
    release_year = Column(Integer, nullable=False)
    rating = Column(Float)
    director = Column(String)

    __table_args__ = (
        CheckConstraint('release_year >= 1888', name='check_valid_year'),
        CheckConstraint('rating >= 0 AND rating <= 10', name='check_valid_rating'),
    )