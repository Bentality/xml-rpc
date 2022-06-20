import xmlrpc.client
import sys

webAddress = str(sys.argv[1])
port = str(sys.argv[2])
x = float(sys.argv[3])
y = float(sys.argv[4])

with xmlrpc.client.ServerProxy("http://" + webAddress + ":" + port + "/") as proxy:
    print(str(x) + " + " + str(y) + " is " + str(proxy.add(x, y)))
    print(str(x) + " - " + str(y) + " is " + str(proxy.sub(x, y)))
    print(str(x) + " * " + str(y) + " is " + str(proxy.mul(x, y)))
    print(str(x) + " / " + str(y) + " is " + str(proxy.div(x, y)))
    print(str(proxy.hour()) + ":" + str(proxy.minute()) + ":" + str(proxy.second()))