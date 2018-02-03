from worker.services.scanner import ScanService,PortService

class DummyHandler:
     @classmethod
     def process(cls,*args): pass

class Services:
      _handlers={"ScanService":ScanService,"PortService":PortService}
      def gethandler(handler):
               handler_instance=DummyHandler
               if (handler):
                    handler_instance=Services._handlers[handler]
               return handler_instance