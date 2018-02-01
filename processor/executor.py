from dao.dataaccesslayer import *
from dao.entities import *
import datetime

def getstatus(hash):
        op=dal.Session.query(Operation).filter(Operation.hash==hash).first()
        print(datetime.datetime.now())
        time=(datetime.datetime.now()-op.updated_on).total_seconds()
        print(time)
        if (time<=3600):
            results={'state':op.state,'results':op.results,'date':str(op.updated_on)}
        else:
            results={'state':'No longer Available'}
        return results