import os
import tqdm
import time
import socket
from colorama import Fore, Style, init

success, info, fail, close = Fore.GREEN + Style.BRIGHT, Fore.YELLOW + \
    Style.BRIGHT, Fore.RED + Style.BRIGHT, Style.RESET_ALL


def upload_file(targ_id, file_name):
    BUFFER_SIZE = 8192
    filesize = os.path.getsize(file_name)
    progress = tqdm.tqdm(range(filesize), f"Sending {file_name}", unit="B", unit_scale=True,
                         unit_divisor=1024, bar_format='{l_bar}{bar:20}{r_bar}{bar:-20b}')
    with open(file_name, 'rb') as f:
        while True:
            bytes_read = f.read(BUFFER_SIZE)
            if not bytes_read:
                break
            targ_id.send(bytes_read)
            progress.update(len(bytes_read))
    time.sleep(3)


def download_file(targ_id, file_name):
    file_status = targ_id.recv(1024).decode()
    if file_status == '0':
        print(info + f'[-] That file was not found.' + close)
        pass
    else:
        print(info + f'[+] Downloading {file_name}' + close)
        try:
            f = open(file_name, 'wb')
            targ_id.settimeout(5)
            chunk = targ_id.recv(8192)
            while chunk:
                f.write(chunk)
                try:
                    chunk = targ_id.recv(8192)
                except socket.timeout as e:
                    break
            targ_id.settimeout(None)
            f.close()
            if os.path.exists(file_name):
                print(
                    success + f'[+] {file_name} downloaded successfully.' + close)
            else:
                print(fail + f'[-] An error occurred during download.')
        except OSError:
            pass
