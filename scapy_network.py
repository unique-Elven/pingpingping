# -*- coding:utf-8 -*-
from scapy.all import *
from scapy.layers.inet import ICMP, IP
import time


def scapy_ping(ip):
    loss = 0
    for i in range(4):
        packet = IP(dst=ip, ttl=128) / ICMP()
        ping = sr1(packet, timeout=0.2, verbose=False)
        if not ping:
            loss += 1
    # 丢包率
    probability = str(loss/4) + '%'
    return True, probability


if __name__ == '__main__':
    print(scapy_ping('192.168.18.194'))
