import threading
from dao.dataaccesslayer import addport

class Port:
      def __init__(self):
           self.results={}
      def worker(self,services):
          for name,port in services.items():
              self.results[port]=addport(name,port)
          return self.results
class Scanner:
    _most_used_ports = {
        '21': 'FTP',
        '22': 'SSH',
        '23': 'TELNET',
        '25': 'SMTP',
        '53': 'DNS',
        '69': 'TFTP',
        '80': 'HTTP',
        '109': 'POP2',
        '110': 'POP3',
        '123': 'NTP',
        '137': 'NETBIOS-NS',
        '138': 'NETBIOS-DGM',
        '139': 'NETBIOS-SSN',
        '143': 'IMAP',
        '156': 'SQL-SERVER',
        '389': 'LDAP',
        '443': 'HTTPS',
        '546': 'DHCP-CLIENT',
        '547': 'DHCP-SERVER',
        '995': 'POP3-SSL',
        '993': 'IMAP-SSL',
        '2086': 'WHM/CPANEL',
        '2087': 'WHM/CPANEL',
        '2082': 'CPANEL',
        '2083': 'CPANEL',
        '3306': 'MYSQL',
        '8443': 'PLESK',
        '10000': 'VIRTUALMIN/WEBMIN'
    }

    def __init__(self):
        self.results = {}


    @classmethod
    def most_used_ports(cls):
        return Scanner._most_used_ports.keys()


    @classmethod
    def getallservices(cls):
        return Scanner._most_used_ports

    @classmethod
    def getsomeservices(cls, ports=[]):
        result = dict()
        for port in ports:
            port = [port, port[1:]][port[0] == '/']
            if port in Scanner.most_used_ports():
                result[port] = Scanner._most_used_ports[port]
            else:
                result[port] = "unknown"
        return result

    def getportstatus(self, host, port):
        import socket
        code = 1
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.3)
            code = s.connect_ex((host, int(port)))
        finally:
            s.close()
            return (code == 0)

    def worker(self, host, ports):
        self.results[host] = dict()
        for port in ports:
            self.results[host][port] = ["closed","open"][self.getportstatus(host, port)]


class ScanService:
   @classmethod
   def process(cls,hosts):
      print("Invocando al scanner",hosts)
      _threads = []
      sc = Scanner()
      try:
        for host in hosts.keys():
            t = threading.Thread(target=sc.worker,
                             args=(host, [hosts[host],Scanner.most_used_ports()][len(hosts[host]) == 0]))
            t.start()
            _threads.append(t)
        [t.join() for t in _threads]
      finally:
               return sc.results

class PortService:
      @classmethod
      def process(cls,*args):
          p=Port()
          p.worker(*args)
          return p.results




