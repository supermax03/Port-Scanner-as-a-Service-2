from worker.services.scanner import ScanService

class DummyHandler:
     @classmethod
     def process(cls,*args): pass

class Services:
      _handlers={"ScanService":ScanService}
      def gethandler(handler):
               handler_instance=DummyHandler
               if (handler):
                    handler_instance=Services._handlers[handler]
               return handler_instance