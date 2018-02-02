from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dao.instance.config import app_config
from dao.entities import *


class DataAccessLayer:
    def __init__(self):
        self.engine = create_engine(app_config['development'].SQLALCHEMY_DATABASE_URI)
        self._session = sessionmaker(bind=self.engine)()
        Base.metadata.create_all(self.engine)  # Sino existe se crea toda la base de datos

    def session(self):
        return self._session

    Session = property(fget=session)


dal = DataAccessLayer()


def validateop(op):
    task = dal.Session.query(Task).filter(Task.name == op['operation']).first()
    return (task != None)


def gettaskid(op):
    task = dal.Session.query(Task).filter(Task.name == op[0]['operation']).first()
    return task.taskid


def getoperation(hash):
    op = dal.Session.query(Operation).filter(Operation.hash == hash).first()
    return op

def getrequeriments():
    query = dal.Session.query(Operation.task_id,
                              Operation.hash,
                              Operation.requeriment,
                              Operation.state,
                              Task.handler)
    query = query.join(Task).order_by(Task.priority)
    results = query.filter(Operation.state == 'Pending').limit(10)
    return results

def updateoperation(hash,results):
  try:
      operation = dal.Session.query(Operation).get(hash)
      operation.results = results
      operation.state = 'Done'
      dal.Session.add(operation)
      dal.Session.commit()
  except:
      dal.Session.rollback()


def addoperation(data):
    try:
        if not (getoperation(data["idreq"])):
                   operation=Operation(hash=data["idreq"],
                   task_id=data["taskid"],
                   requeriment = data["payload"]
                   )
                   dal.Session.add(operation)
                   dal.Session.commit()
    except:
            dal.Session.rollback()