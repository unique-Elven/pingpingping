# -*- coding:utf-8 -*-
from scapy.all import *
from random import randint
import sys
import multiprocessing
import ipaddress
from scapy.layers.inet import ICMP, IP
from scapy.layers.l2 import Ether
import time


def scapy_ping_one(host):
    id_ip = randint(1, 65535)
    id_ping = randint(1, 65535)
    seq_ping = randint(1, 65535)
    packet = IP(dst=host, ttl=128, id=id_ip) / ICMP(id=id_ping, seq=seq_ping)
    ping = sr1(packet, timeout=0.2, verbose=False)
    if ping:
        os._exit(3)


def scapy_ping(ip):
    ping_one = multiprocessing.Process(target=scapy_ping_one, args=(ip,))
    ping_one.start()
    time.sleep(0.3)
    if ping_one.exitcode == 3:
        return True
    else:
        ping_one.terminate()
    return False


if __name__ == '__main__':
    print(scapy_ping('192.168.18.194'))
