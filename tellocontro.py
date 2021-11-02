from flask import Flask, request, render_template
import socket
import time

'''host = ''
port = 9000
locaddr = (host,port)'''
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
tello_address = ('192.168.10.1',8889)

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def submit():
    if request.method == 'POST':
        cmds=request.values.get('cmds')
        y = cmds.split("_")
        
        for i in range(len(y)):
            if y[i] == "1":
                sock.sendto(b"command", tello_address)
                response, ip = sock.recvfrom(1024)
                print("command: ",response)
                time.sleep(1)
            elif y[i] == "2":
                sock.sendto(b"takeoff", tello_address)
                response, ip = sock.recvfrom(1024)
                print("takeoff: ",response)
                time.sleep(3)
            elif y[i] == "3":
                sock.sendto(b"battery?", tello_address)
                response, ip = sock.recvfrom(1024)
                print("battery? ",response)
                time.sleep(1)
            elif y[i] == "4":
                sock.sendto(b"land", tello_address)
                response, ip = sock.recvfrom(1024)
                print("land: ",response)
                time.sleep(1)
            #elif y[i] == "5":
        sock.close() 
    return render_template("index.html")

if __name__=="__main__":
    app.run()
    