from xmlrpc.server import SimpleXMLRPCServer
import sys
import datetime as dt

ip_address = str(sys.argv[1])
port = int(sys.argv[2])

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    if y == 0:
        return "Infinity"
    else:
        return x / y

def hour():
    return dt.datetime.now().hour

def minute():
    return dt.datetime.now().minute

def second():
    return dt.datetime.now().second

server = SimpleXMLRPCServer((ip_address, port))
print("Listening on port %s...", str(port))
server.register_function(add, "add")
server.register_function(sub, "sub")
server.register_function(mul, "mul")
server.register_function(div, "div")
server.register_function(hour, "hour")
server.register_function(minute, "minute")
server.register_function(second, "second")
server.serve_forever()