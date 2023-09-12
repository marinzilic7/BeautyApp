from __init__ import Base
from datetime import datetime
from sqlalchemy import *


class Termin (Base):
    __tablename__ = "termin"
    ID_termin = Column(Integer, primary_key = True)
    korisnik_id = Column(Integer, ForeignKey('korisnici.ID_korisnika'))
    datum_termina = Column(DateTime, default=datetime.now)
