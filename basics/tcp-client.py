import socket

target_host = "www.google.com"
target_port = 80
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