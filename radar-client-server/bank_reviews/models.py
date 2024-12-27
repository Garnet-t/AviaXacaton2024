import os
from sqlalchemy import Column, Integer, String, Text, DateTime, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

DB_URL = os.getenv("DB_URL")

Base = declarative_base()


class BankReview(Base):
    __tablename__ = 'bank_reviews'

    id = Column(Integer, primary_key=True)
    bank_id = Column(Integer, nullable=False)
    title = Column(String, nullable=False)
    text = Column(Text, nullable=False)
    review_date = Column(DateTime, nullable=False)
    rating = Column(Integer, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<BankReview(id={self.id}, bank_id={self.bank_id}, title='{self.title}')>"


def get_engine():
    if not DB_URL:
        raise ValueError("Database URL is not set in .env")
    return create_engine(DB_URL)


def get_session(engine):
    Session = sessionmaker(bind=engine)
    return Session()


def init_db():
    engine = get_engine()
    Base.metadata.create_all(engine)
    print("Database initialized successfully.")
