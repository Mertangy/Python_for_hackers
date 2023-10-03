import socket

target_host = "127.0.0.1"
target_port = 9999

#Create a socket object
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#Connect client
try:
    client.connect((target_host,target_port))
    print(f"Connected to {target_host}:{target_port}")
except socket.error as e:
    print(f"Connection to {target_host}:{target_port} failed.{e}")
    exit()


#send come data
client.sendto(("GET / HTTP/1.1\r\nHost: google.com\r\n\r\n").encode(),(target_host,target_port))

#receive data
response = client.recv(4096)

if response:
    print(f"Recieved from server: {response.decode()}")

# close the socket
client.close()