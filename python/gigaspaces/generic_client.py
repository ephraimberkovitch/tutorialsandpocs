import sys
import socket
import redis
from time import sleep

class GenericClient:
    def connect(self,constr):
        pass

    def send(self,command):
        pass

class SocketClient(GenericClient):
    def __init__(self,constr):
        tokens = constr.split(':')
        self.server = tokens[0]
        self.port = int(tokens[1])

    def send(self,command):
        # Create a TCP/IP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Connect the socket to the port where the server is listening
        server_address = (self.server, self.port)
        print >> sys.stderr, 'connecting to %s port %s' % server_address
        sock.connect(server_address)

        try:

            # Send data
            print >> sys.stderr, 'sending "%s"' % command
            sock.sendall(command)

            data = sock.recv(1024)
            print >> sys.stderr, 'received "%s"' % data

        finally:
            print >> sys.stderr, 'closing socket'
            sock.close()


class RedisClient(GenericClient):
    def __init__(self, host, port, queue_name):
        self.redis = redis.Redis(host=host, port=port)
        self.queue = queue_name

    def send(self,command):
        self.redis.rpush(self.queue,command)
        sleep(1)
        cnt = 1
        response = self.redis.get(command)
        while (not response) and cnt<60:
            cnt +=1
            response = self.redis.get(command)
        if response:
            print >> sys.stderr, 'received "%s"' % response
        else:
            print >> sys.stderr, 'timeout reached'

if __name__== '__main__':

    if len(sys.argv)>2:
        constr = sys.argv[1]
        command = sys.argv[2]
    else:
        constr = 'localhost:1000'
        command = 'time'

    client = SocketClient(constr)
    client.send(command)
    '''
    client = RedisClient('redis-10024.c9.us-east-1-4.ec2.cloud.redislabs.com',10024,'queue')
    client.send('ping')
    '''