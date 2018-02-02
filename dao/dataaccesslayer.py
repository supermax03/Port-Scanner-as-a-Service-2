from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dao.instance.config import app_config
from dao.entities import *


class DataAccessLayer:
    def __init__(self):
        self.engine = create_engine(app_config['development'].SQLALCHEMY_DATABASE_URI)
        self.session = sessionmaker(bind=self.engine)()
        Base.metadata.create_all(self.engine)  # Sino existe se crea toda la base de datos

    def session(self):
        return self.session

    Session = property(fget=session)


dal = DataAccessLayer()


def validateop(op):
    task = dal.Session.query(Task).filter(Task.name == op['operation']).first()
    return (task != None)


def gettaskid(op):
    task = dal.Session.query(Task).filter(Task.name == op[0]['operation']).first()
    print(task)
    return task.taskid


def getoperation(hash):
    op = dal.Session.query(Operation).filter(Operation.hash == hash).first()
    return op
