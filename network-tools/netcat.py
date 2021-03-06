import shlex
import socket
import subprocess
import argparse
import textwrap
import sys
import threading

def execute(cmd):
    print("Inside execute()")
    cmd = cmd.strip()
    
    if not cmd:
        return
    
    output = subprocess.check_output(shlex.split(cmd), stderr = subprocess.STDOUT)
    return output.decode()

class Netcat:
    def __init__(self, args, buffer=None):
        self.args = args
        self.buffer = buffer
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    def run(self):
        print("Inside run()")
        if self.args.listen:
            self.listen()
        else:
            self.send()
    
    def send(self):
        print("Inside send()")
        self.socket.connect((self.args.target, self.args.port))
        if self.buffer:
            self.socket.send(self.buffer)
        
        try:
            while True:
                recv_len = 1
                response = ''
                while recv_len:
                    data = self.socket.recv(4096)
                    recv_len = len(data)
                    response += data.decode()
                    if recv_len < 4096:
                        break
                if response:
                    print(response)
                    buffer = input('> ')
                    buffer += '\n'
                    self.socket.send(buffer.encode())

        except KeyboardInterrupt:
            print("User Terminated")
            self.socket.close()
            sys.exit()

    def listen(self):
        print("Inside Listen")
        self.socket.bind((self.args.target, self.args.port))
        self.socket.listen(5)

        while True:
            client_socket, _ = self.socket.accept()
            client_thread = threading.Thread(target=self.handle, args=(client_socket,))
            client_thread.start()

    def handle(self, client_socket):
        print("Inside Handle")
        if self.args.execute:
            output = execute(self.args.execute)
            client_socket.send(output.encode())

        elif self.args.upload:
            print("inside upload")
            file_buffer = b''
            while True:
                print("inside while uplosd")
                data = client_socket.recv(4096)
                print(len(data))
                if data:
                    print("inside if data")
                    file_buffer += data
                else:
                    break
            
            with open(self.args.upload, 'wb') as f:
                f.write(file_buffer)
            
            message = f"Saved file {self.args.upload}"
            client_socket.send(message.encode())
        
        elif self.args.command:
            print("Inside command")
            cmd_buffer = b''
            while True:
                try:
                    client_socket.send(b'cmd: #> ')
                    while '\n' not in cmd_buffer.decode():
                        cmd_buffer += client_socket.recv(64)
                    
                    response = execute(cmd_buffer.decode())
                    
                    if response:
                        client_socket.send(response.encode())

                    cmd_buffer = b''

                except Exception as e:
                    print(f"Server killer {e}")
                    self.socket.close()
                    sys.exit()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Netcat Pytool v1", formatter_class=argparse.RawDescriptionHelpFormatter, epilog=textwrap.dedent(
        '''
        Example:
        CTRL-Z instead of CTRL-D in windows
        netcat.py -t 192.168.1.108 -p 5555 -l -c # command shell
        netcat.py -t 192.168.1.108 -p 5555 -l -u=mytest.txt # upload to a file
        netcat.py -t 192.168.1.108 -p 5555 -l -e=\"cat /etc/passwd\" # execute command
        echo 'ABC' | ./netcat.py -t 192.168.1.108 -p 135 # echo text to server port 135
        netcat.py -t 192.168.1.108 -p 5555 # connect to server
        '''
    ))
    parser.add_argument("-c", "--command", action="store_true", help="command shell")
    parser.add_argument("-e", "--execute", help="execute specific command")
    parser.add_argument("-l", "--listen", action="store_true", help="listen")
    parser.add_argument("-t", "--target", help="specified IP")
    parser.add_argument("-p", "--port", type=int, help="specified port", default=5555)
    parser.add_argument("-u", "--upload", help="upload file")
    args = parser.parse_args()

    print("Inside Main")
    print(args)
    if args.listen:
        buffer = ""
    else:
        buffer = sys.stdin.read()

    nc = Netcat(args, buffer.encode())
    nc.run()
