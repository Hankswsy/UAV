import socket
import time

def command():
    sock.sendto(b"command", tello_address)
    response = sock.recvfrom(1024)
    print("command: ",response)

def takeoff():
    sock.sendto(b"takeoff", tello_address)
    response = sock.recvfrom(1024)
    print("takeoff: ",response)
    time.sleep(3)

def land():
    sock.sendto(b"land", tello_address)
    response = sock.recvfrom(1024)
    print("land: ",response)

def battery():
    sock.sendto(b"battery?", tello_address)
    response = sock.recvfrom(1024)
    print("battery? ",response)



    

if __name__ == '__main__':
    host = ''
    port = 9000
    locaddr = (host,port)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    tello_address = ('192.168.10.1',8889)
    sock.bind(locaddr)