from __init__ import Base

from sqlalchemy import *


class Proizvod (Base):
    __tablename__ = "proizvod"
    ID_proizvoda = Column(Integer, primary_key = True)
    ime = Column(String(50))
    kategorija =Column(String(50))
  