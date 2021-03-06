from dao.dataaccesslayer import *
from myutils.utils import isexpiredtoken, gethash
from processor import sender
import sys
import json


def getservices(service):
    items = []
    print(service)
    for svc in getservices_def(service):
        item = {'name': svc.name,
                'port': svc.port}
        items.append(item)
    if len(items) > 0:
        code=200
    else:
        code=404
    results={'results':items,'code':code}
    return results


def getstatus(hash):
    try:
        op = getoperation(hash)
        if (op):
            if not isexpiredtoken(op.updated_on):
                results = {"state": op.state,
                           "results": op.results,
                           "date": str(op.updated_on),
                           "code": 200}
            else:
                results = {"state": "No longer Available",
                           "code": 200}
        else:
            results = {"state": "Not found",
                       "code": 404}
    except:
        results = {"state": "Internal server Error",
                   "exception": str(sys.exc_info()[1]), "code": 500}
    finally:
        return results


def addOperation(op):
    try:

        if (validateop(op)):
            op = [op]
            op[0]['idreq'] = gethash()
            op[0]['taskid'] = gettaskid(op)
            msg = json.dumps(op)
            print(msg)
            sender.send(msg)
            results = {"state": 'Operacion Valida',
                       "code": 200,
                       "yourid": op[0]['idreq'],
                       "payload": op[0]['payload'],
                       "operation": op[0]['operation']}
        else:
            results = {"state": 'Operacion Invalida',
                       "code": 404
                       }

    except:
        results = {"state": "Internal server Error",
                   "exception": str(sys.exc_info()[1]), "code": 500}
    finally:
        return results
