from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dao.instance.config import app_config
from dao.entities import Base


class DataAccessLayer:
    def __init__(self):
        self.engine = create_engine(app_config['development'].SQLALCHEMY_DATABASE_URI)
        self.session = sessionmaker(bind=self.engine)()
        Base.metadata.create_all(self.engine)  # Sino existe se crea toda la base de datos

    def session(self):
        return self.session

    Session = property(fget=session)


dal = DataAccessLayer()
