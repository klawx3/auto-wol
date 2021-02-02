from icmplib import ping
from time import sleep
from pywol import wake
from os import environ

TIMEOUT = int(environ['TIMEOUT'])
HOST = environ['HOST']
MAC  = environ['MAC']
BROADCAST = environ['BROADCAST']

while True:
    host = ping(HOST,count=1,interval=1,timeout=TIMEOUT)
    sleep(TIMEOUT)
    if host.is_alive:
        print("Host:{}\tRTT avg:{}\tPacket Loss:{}".format(host.address,host.avg_rtt,host.packet_loss))
    else:
        print("Host:{} Death... sending WOL -> MAC: {}\tBROADCAST:{} ".format(HOST,MAC,BROADCAST))
        wake(MAC,ip_address=BROADCAST)
