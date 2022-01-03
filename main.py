import socket
from fdp import ForzaDataPacket
import winsound
import time
import threading
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('', 9908))
condition = threading.Event()
is_enable = False

def play():
    time.sleep(5)
    while not condition.is_set():
        winsound.PlaySound("ae86.wav", winsound.SND_ALIAS)
        
while True:
    message, address = server_socket.recvfrom(1024)
    fdp = ForzaDataPacket(message, packet_format = 'fh4')
    if fdp.car_ordinal == 455 and (round((fdp.speed * 2.23694 * 1.60934), 2)) > 120:
        if not is_enable:
            condition = threading.Event()
            x = threading.Thread(target=play)
            x.start()
            
            is_enable = True

    else: 
        
        if is_enable:
            condition.set()  
        is_enable = False
        
