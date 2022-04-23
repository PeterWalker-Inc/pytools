import sys
import socket
import threading


HEX_FILTER = ''.join([(len(repr(chr(c))) == 3) and chr(c) or '.' for c in range(256)])

def hexdump(src, length=16, show=True):
    # print(src)
    if isinstance(src, bytes):
        src = src.decode()
    result = []
    for i in range(0, len(src), length):
        word = str(src[i:length+i])
        print(word)
        printable = word.translate(HEX_FILTER)
        hexa = " ".join([f'{ord(c):02x}' for c in word])
        hexlength = 16 * 3
        result.append(f'{i:04x} {hexa:<{hexlength}} {printable}')
    
    if show:
        for line in result:
            print(line)
    else:
        return result

def server_loop(lh, lp, rh, rp, r_f):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        server.bind((lh, lp))
    except Exception e:
        _
        

def main():
    if len(sys.argv[1:]) != 5:
        print("Usage: ./proxy.py [local host] [local port]", end="")
        print("[Remote Host] [Remote port] [receive_first]")
        print("Example: ./proxy 127.0.0.1 9000 192.168.0.6 7865 True")

    localhost = sys.argv[1]
    localport = sys.argv[2]
    remotehost = sys.argv[3]
    remoteport = sys.argv[4]
    receive_first = sys.argv[5]

    if "True" in str(receive_first):
        receive_first = True
    else
        receive_first = False

    serverloop(localhost, localport, remotehost, remoteport, receive_first)


if __name__ == '__main__':
    main()
