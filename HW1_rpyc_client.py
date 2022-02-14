import rpyc
import sys
 
if len(sys.argv) < 2:
   exit("Usage {} SERVER".format(sys.argv[0]))
 
server = sys.argv[1]
 
conn = rpyc.classic.connect(server)

array = [9, 4, 3, 5, 1, 7, 2, 0, 6, 8]

print(array)

string_program = """def alg(array):
   c = len(array)
   for i in range(c-1):
      for y in range(0, c-i-1):
         if array[y] > array[y+1]:
            array[y], array[y+1] = array[y+1], array[y]

"""

conn.execute(string_program)
conn.namespace["alg"](array)
conn.eval("alg")

print(array)

rsys = conn.modules.sys
print(rsys.version)
