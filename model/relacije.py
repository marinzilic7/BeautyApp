
from sqlalchemy.orm import relationship
from korisnici import Korisnik
from proizvodi import Proizvod
from studio import Studio
from termin import Termin
from recenzije import Recenzija
from __init__ import Base
from __init__  import engine


Korisnik.termin = relationship('Termin', back_populates='korisnik')
Korisnik.recenzija = relationship("Recenzija", back_populates="korisnik")
Termin.recenzija = relationship("Recenzija", back_populates="termin")


Base.metadata.bind = engine
Base.metadata.create_all(bind=engine)