import rpyc
import sys
 
if len(sys.argv) < 2:
   exit("Usage {} SERVER".format(sys.argv[0]))
 
server = sys.argv[1]

conn = rpyc.connect(server, 18812)
print(conn.root.exposed_test_random("it works!"))