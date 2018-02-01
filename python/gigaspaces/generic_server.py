import sys
import socket
import redis
import generic_command
from time import sleep
import threading

class GenericServer:
    def listen(self):
        pass

    def process_command(self,command_text):
        command = generic_command.GenericCommand.parse_command(command_text)
        return command

class SocketServer(GenericServer):
    def __init__(self,port):
        self.port = port

    def listen(self):
        # Create a TCP/IP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Bind the socket to the port
        server_address = ('localhost', self.port)
        print >> sys.stderr, 'starting up on %s port %s' % server_address
        sock.bind(server_address)

        # Listen for incoming connections
        sock.listen(1)
        while True:
            # Wait for a connection
            print >>sys.stderr, 'waiting for a connection'
            connection, client_address = sock.accept()
            try:
                print >> sys.stderr, 'connection from', client_address
                command_text = connection.recv(16)
                print >> sys.stderr, 'received "%s"' % command_text
                if command_text:
                    print >> sys.stderr, 'sending data back to the client'
                    command = generic_command.GenericCommand.parse_command(command_text)
                    connection.sendall(command.response())
                else:
                    print >> sys.stderr, 'empty request'
            finally:
                # Clean up the connection
                connection.close()

    def listen_with_threads(self):
        # Create a TCP/IP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Bind the socket to the port
        server_address = ('localhost', self.port)
        print >> sys.stderr, 'starting up on %s port %s' % server_address
        sock.bind(server_address)

        # Listen for incoming connections
        sock.listen(1)
        while True:
            # Wait for a connection
            print >>sys.stderr, 'waiting for a connection'
            connection, client_address = sock.accept()
            try:
                print >> sys.stderr, 'connection from', client_address
                command_text = connection.recv(16)
                processing = threading.Thread(self.generate_response,args=(connection,command_text))
                processing.start()
            finally:
                # Clean up the connection
                connection.close()

    @staticmethod
    def generate_response(connection,command_text):
        print >> sys.stderr, 'received "%s"' % command_text
        if command_text:
            print >> sys.stderr, 'sending data back to the client'
            command = generic_command.GenericCommand.parse_command(command_text)
            connection.sendall(command.response())
        else:
            print >> sys.stderr, 'empty request'


class RedisServer(GenericServer):
    def __init__(self,host,port,queue):
        self.redis = redis.Redis(host=host, port=port)
        self.queue = queue

    def listen(self):
        print >> sys.stderr, 'starting up listening...'
        while True:
            command_texts = self.redis.lrange(self.queue,0,-1)
            self.redis.delete(self.queue)
            for command_text in command_texts:
                print >> sys.stderr, 'received "%s"' % command_text
                command = self.process_command(command_text)
                response = command.response()
                print >> sys.stderr, 'sending back "%s"' % response
                self.redis.set(command_text,response)
            sleep(1)


if __name__== '__main__':

    if len(sys.argv)>1:
        port = int(sys.argv[1])
    else:
        port = 1000
    server = SocketServer(port)
    server.listen()
    '''
    server = RedisServer('redis-10024.c9.us-east-1-4.ec2.cloud.redislabs.com',10024,'queue')
    server.listen()
    '''