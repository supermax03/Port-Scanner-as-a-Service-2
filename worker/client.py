from dao.dataaccesslayer import dal
from dao.entities import *

lista=dal.Session.query(Services).all()
for item in lista:
     print(item.name)

item=Services(port='22',name='TELNET')
dal.session.add(item)
dal.session.commit()
result = dal.Session.query(Services).filter(Services.port=='22').all()
print(result)

item=Task(taskid=2,name="Port Scan",priority=2,handler="ScanService")
dal.session.add(item)
dal.session.commit()

item=Task(taskid=1,name="Add Port",priority=1)
dal.session.add(item)
dal.session.commit()

item=Task(taskid=3,name="Custom",priority=3)
dal.session.add(item)
dal.session.commit()


result = dal.Session.query(Task).filter(Task.taskid==1).all()
print(result)

item=Operation(hash='zzzzzzzzzz',task_id=3,requeriment='{host:{machine},ports:[222,233,445]}',results='{222:open,233:open,445:open}')
dal.session.add(item)
dal.session.commit()

item=Operation(hash='121323131233212213primero',task_id=1,requeriment='{host:{machine},ports:[22,23,45]}',results='{22:open,23:open,45:open}')
dal.session.add(item)
dal.session.commit()

item=Operation(hash='1232132353647895segundo',task_id=2,requeriment='{host:{machine},ports:[22,23,45]}',results='{22:open,23:open,45:open}')
dal.session.add(item)
dal.session.commit()


result = dal.Session.query(Operation).filter(Operation.hash=='12132313123213').all()
print(result)




