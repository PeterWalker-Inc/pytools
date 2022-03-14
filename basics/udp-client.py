import socket

target_host = "127.0.0.1"
target_port = 8888

#socket creation
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#send
client.sendto(b"Hello There you ***", (target_host, target_port))

#recv
data, address = client.recvfrom(4096)
print(address)
print(data.decode())

client.close()