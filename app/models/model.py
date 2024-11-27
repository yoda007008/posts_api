from sqlalchemy import Boolean, Column, Integer, String
from app.database import Base


class Posts(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True, index=True, nullable=False)
    text = Column(String, nullable=False)
    like = Column(Boolean, nullable=False)


