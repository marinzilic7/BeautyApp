from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine("mysql+pymysql://root@localhost:3306/studio")


Session = sessionmaker(bind=engine)

Session = Session()

Base = declarative_base()