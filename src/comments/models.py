from src.app.database import Base
from sqlalchemy import Column, String, Integer, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import text as sa_text


# FILM COMMENT TABLE
class FilmComment(Base):
    __tablename__ = "film_comment"
    id = Column(Integer, primary_key=True, nullable=False)
    text = Column(String(length=500), nullable=False)
    film_id = Column(Integer, ForeignKey("films.id", ondelete="CASCADE"))
    date_created = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=sa_text("now()")
    )
    film = relationship("Film")
