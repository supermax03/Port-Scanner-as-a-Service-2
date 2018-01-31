from dao.dataaccesslayer import dal
from dao.entities import *
from worker.services.Services import Services
import threading


class BackgroundWorker:

    @classmethod
    def callback(cls):
        results = BackgroundWorker.get_req()
        for item in results:
            handler = Services.gethandler(item.handler)
            results = handler.process(item.requeriment)
            if (results):
                BackgroundWorker.update(item.hash,results)
        BackgroundWorker.listening()

    @classmethod
    def update(cls,hash,results):
        operation=dal.Session.query(Operation).get(hash)
        operation.results=results
        operation.state='Done'
        dal.Session.add(operation)
        dal.Session.commit()
    @classmethod
    def get_req(cls):
        query = dal.Session.query(Operation.task_id,
                                  Operation.hash,
                                  Operation.requeriment,
                                  Operation.state,
                                  Task.handler)
        query = query.join(Task).order_by(Task.priority)
        results = query.filter(Operation.state == 'Pending').limit(10)
        return results

    @classmethod
    def listening(cls):
        t = threading.Timer(2, BackgroundWorker.callback)
        t.start()

def start():
    BackgroundWorker.listening()


start()
