from datetime import datetime
from sqlalchemy import Column, String, DateTime, JSON, Integer, ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Task(Base):
    __tablename__ = 'tasks'
    taskid = Column(Integer(), primary_key=True)
    name = Column(String(30), nullable=False)
    created_on = Column(DateTime(), default=datetime.now)
    updated_on = Column(DateTime(), default=datetime.now, onupdate=datetime.now)
    priority = Column(Integer(), nullable=False)
    handler=Column(String(100))

    def __repr__(self):
        return "Operation(taskid={self.taskid}, " \
               "name={self.name}, " \
               "priority={self.priority}, " \
               "created_on={self.created_on}, " \
               "updated_on={self.updated_on})".format(self=self)


class Operation(Base):
    __tablename__ = 'operations'
    hash = Column(String, primary_key=True)
    created_on = Column(DateTime(), default=datetime.now)
    updated_on = Column(DateTime(), default=datetime.now, onupdate=datetime.now)
    state = Column(String(10), default='Pending')
    task_id = Column(Integer(), ForeignKey('tasks.taskid'), nullable=False)
    requeriment = Column(JSON, nullable=False)
    results = Column(JSON, nullable=True)
    task = relationship("Task", backref=backref('operations',order_by=Task.priority))

    def __repr__(self):
        return "Operation(hash={self.hash}, " \
               "state={self.state}, " \
               "requirement={self.requeriment}, " \
               "results={self.results}, " \
               "task_id={self.task_id}, " \
               "created_on={self.created_on}, " \
               "updated_on={self.updated_on})".format(self=self)


class Services(Base):
    __tablename__ = 'services'
    port = Column(String(5), primary_key=True)
    name = Column(String(100))
    created_on = Column(DateTime(), default=datetime.now)
    updated_on = Column(DateTime(), default=datetime.now, onupdate=datetime.now)

    def __repr__(self):
        return "Services(port={self.port}, " \
               "name={self.name}, " \
               "created_on={self.created_on}, " \
               "updated_on={self.updated_on})".format(self=self)
