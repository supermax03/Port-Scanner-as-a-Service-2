from dao.dataaccesslayer import *
from dao.entities import *
from myutils.utils import isexpiredtoken

def getstatus(hash):
     op=dal.Session.query(Operation).filter(Operation.hash==hash).first()
     if (op):
              if not isexpiredtoken(op.updated_on):
                  results = {'state': op.state, 'results': op.results, 'date': str(op.updated_on),'code':200}
              else:
                  results = {'state': 'No longer Available','code':200}
     else:
                results={'state':'Not found','code':404}
     return results

