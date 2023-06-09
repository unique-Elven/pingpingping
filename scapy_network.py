# -*- coding:utf-8 -*-
from scapy.all import *
from scapy.layers.inet import ICMP, IP
import time


def scapy_ping(ip):
    loss = 0
    ip = str(ip)
    for i in range(4):
        packets = IP(dst=ip, ttl=128) / ICMP()
        ping = sr1(packets, timeout=0.2, verbose=False)
        if not ping:
            loss += 1
            continue
        if ping[ICMP].type:
            loss += 1

    # 丢包率
    probability = str(loss / 4 * 100) + '%'
    if probability == '100.0%':
        return False, probability
    return True, probability


if __name__ == '__main__':
    print(scapy_ping('192.168.18.191'))
