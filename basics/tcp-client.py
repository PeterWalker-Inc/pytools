import socket

target_host = "127.0.0.1"
target_port = 9998
payload = b"GET / HTTP/1.1\r\nHost: www.google.com\r\n\r\n"
#create a socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connect 
client.connect((target_host, target_port))

#send data
client.send(payload)

#recv
response = client.recv(4096)

print(response.decode())
client.close()