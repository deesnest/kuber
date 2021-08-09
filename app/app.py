from flask import Flask
import socket
app = Flask(__name__)
@app.route('/')
def hello():
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    return local_ip
if __name__ == '__main__':
   app.run(host="0.0.0.0", port=80)
