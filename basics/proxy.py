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

def receive_from(connection):
    buffer = b""
    connection.settimeout(5)

    try:
        while True:
            data = connection.recv(4096)
            if not data:
                break
            buffer += data
    except Exception as e:
        pass
    return buffer


def response_handler(buffer):
    # ###
    return buffer

def request_handler(buffer):
    # ###
    return buffer

def proxy_handler(client_socket, remote_host, remote_port, receive_first):
    remote_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    remote_socket.connect(remote_host, remote_port)

    if receive_first:
        remote_buffer = receive_from(remote_socket)
        hexdump(remote_buffer)

    remote_buffer = response_handler(remote_buffer)
    if len(remote_buffer):
        print("[<==] Sending %d bytes to local host." % len(remote_buffer))
        client_socket.send(remote_buffer)

    while True:
        local_buffer = receive_from(client_socket)
        if len(local_buffer):
            line = "[==>] Received %d bytes from localhost." % len(local_buffer)
            print(line)
            hexdump(local_buffer)

            local_buffer = request_handler(local_buffer)
            remote_socket.send(local_buffer)
            print("[==>] Send to remote.")
        
        remote_buffer = receive_from(remote_socket)
        if len(remote_buffer):
            print("[<==] Received %d bytes from remote." % len(remote_buffer))
            hexdump(remote_buffer)

            remote_buffer = response_handler(remote_buffer)
            client_socket.send(remote_buffer)
            print("[<==] Send to localhost.")

        if not len(local_buffer) or not len(remote_buffer):
            client_socket.close()
            remote_socket.close()
            print("[*] No more data. Closing connections.")
            break

def server_loop(lh, lp, rh, rp, r_f):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    
    try:
        server.bind((lh, lp))
    except Exception as e:
        print("Problem on bind: %r" % e)
        print("[!!] Failed to listen sockets on %s:%d" % (lh, lp))
        print("[!!] Check for permissions or other listeneing sockets")
        sys.exit(0)
    
    print("[!!] Listening on %s:%d" % (lh, lp)) 
    server.listen(5)

    while True:
        client_socket, addr = server.accept()
        line = "> Received incoming connections from %s:%d" % (addr[0], addr[1])
        print(line)
        proxy_thread = threading.Thread(
            target=proxy_handler,
            args = (client_socket, rh, rp, r_f)
        )
        proxy_thread.start()


def main():
    if len(sys.argv[1:]) != 5:
        print("Usage: ./proxy.py [local host] [local port]", end="")
        print("[Remote Host] [Remote port] [receive_first]")
        print("Example: ./proxy 127.0.0.1 9000 192.168.0.6 7865 True")

    localhost = sys.argv[1]
    localport = int(sys.argv[2])
    remotehost = sys.argv[3]
    remoteport = int(sys.argv[4])
    receive_first = sys.argv[5]

    if "True" in str(receive_first):
        receive_first = True
    else:
        receive_first = False

    server_loop(localhost, localport, remotehost, remoteport, receive_first)

if __name__ == '__main__':
    main()
