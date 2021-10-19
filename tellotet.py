import socket
import time 

host = ''
port = 9000
locaddr = (host,port)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
tello_address = ('192.168.10.1',8889)
#sock.bind(locaddr)

sock.sendto(b"command", tello_address)
response, ip = sock.recvfrom(1024)
print("command: ",response)

sock.sendto(b"takeoff", tello_address)
response, ip = sock.recvfrom(1024)
print("takeoff: ",response)
time.sleep(3)

sock.sendto(b"battery?", tello_address)
response, ip = sock.recvfrom(1024)
print("battery? ",response)

sock.sendto(b"land", tello_address)
response, ip = sock.recvfrom(1024)
print("land: ",response)

sock.close()



