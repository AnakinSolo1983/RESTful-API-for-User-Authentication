"""from typing import Optional
from sqlalchemy.orm import Session
from models import RefreshToken

class RefreshTokenRepository:
    
    def __init__(self, session: Session):
    
        self.session = session

    def find_by_token(self, token: str) -> Optional[RefreshToken]:
    
        return self.session.query(RefreshToken).filter_by(token=token).first()"""




"""from typing import Optional
from sqlalchemy.orm import Session
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class RefreshToken(Base):
    __tablename__ = 'refresh_tokens'

    id = Column(Integer, primary_key=True)
    token = Column(String)

def find_by_token(db: Session, token: str) -> Optional[RefreshToken]:
    return db.query(RefreshToken).filter(RefreshToken.token == token).first()"""