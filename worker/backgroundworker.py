from dao.dataaccesslayer import updateoperation,getrequeriments
from worker.services.Services import Services
import time


class BackgroundWorker:
    _activated = True
    @classmethod
    def on(cls,flag=True):
        BackgroundWorker._activated = flag
    @classmethod
    def listening(cls):
        while BackgroundWorker._activated:
            results = BackgroundWorker.get_req()
            for item in results:
                handler = Services.gethandler(item.handler)
                results = handler.process(item.requeriment)
                if (results):
                    BackgroundWorker.update(item.hash, results)
            time.sleep(3)

    @classmethod
    def update(cls, hash, results):
        updateoperation(hash, results)

    @classmethod
    def get_req(cls):
        return getrequeriments()


def stop():
    print("Frenando....")
    BackgroundWorker.on(False)


def start():
    BackgroundWorker.on()
    BackgroundWorker.listening()

stop()
start()
