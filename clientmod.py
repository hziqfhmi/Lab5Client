import socket

s = socket.socket()
host = "192.168.1.7"
port = 6000

s.connect((host, port))
print ("... Connected!\n")

filename = input(str("Enter file name : "))
file = open(filename,'rb')
data = file.read(1024)
s.send(data)

print("Done sending")
file.close()
s.close()
print("connection closed")
