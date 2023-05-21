from src.app.database import Base
from sqlalchemy import Column, String, Integer, TIMESTAMP, Date, text
from sqlalchemy.orm import relationship

from src.comments.models import FilmComment


# FILM TABLE
class Film(Base):
    __tablename__ = "films"
    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    release_date = Column(Date, nullable=False)
    date_created = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )
    comment = relationship("FilmComment", back_populates="film")
