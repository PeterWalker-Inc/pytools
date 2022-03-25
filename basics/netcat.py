import shlex
import socket
from ssl import SOL_SOCKET
import subprocess
import argparse
import textwrap
import sys

def execute(cmd):
    cmd = cmd.strip()
    
    if not cmd:
        return 1
    
    output = subprocess.check_output(shlex.split(cmd), stderr = subprocess.STDOUT)
    return output.decode()

class Netcat:
    def __init__(self, args, buf=None):
        self.args = args
        self.buf = buf
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Netcat Pytool v1", formatter_class=argparse.RawDescriptionHelpFormatter, epilog=textwrap.dedent(
        '''
        Example:
        netcat.py -t 192.168.1.108 -p 5555 -l -c # command shell
        netcat.py -t 192.168.1.108 -p 5555 -l -u=mytest.txt # upload to file
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

    if args.listen:
        buf = ""
    else:
        buf = sys.stdin.read()

    nc = Netcat(args, buf.encode())
    nc.run()

    

