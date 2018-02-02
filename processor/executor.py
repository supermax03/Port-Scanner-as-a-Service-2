from dao.dataaccesslayer import *
from dao.entities import *
from myutils.utils import isexpiredtoken
import sys


def getstatus(hash):
    try:

        op = dal.Session.query(Operation).filter(Operation.hash == hash).first()
        1 / 0
        if (op):
            if not isexpiredtoken(op.updated_on):
                results = {'state': op.state, 'results': op.results, 'date': str(op.updated_on), 'code': 200}


            else:
                results = {'state': 'No longer Available', 'code': 200}

        else:
            results = {'state': 'Not found', 'code': 404}


    except:
        results = {'state': 'Internal server Error', 'exception': str(sys.exc_info()[1]), 'code': 500}
    finally:

        return results
