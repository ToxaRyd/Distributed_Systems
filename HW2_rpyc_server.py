import rpyc
from rpyc.utils.server import ThreadedServer
import datetime
date_time=datetime.datetime.now()

class MonitorService(rpyc.Service):
 def on_connect(self,conn):
  print("\nconnected on {}".format(date_time))
 
 def on_disconnect(self,conn):
  print("disconnected on {}\n".format(date_time))

 def exposed_call(self, string):
  print(string)

 
if __name__=='__main__':
 
 t=ThreadedServer(MonitorService, port=18812)
 t.start()