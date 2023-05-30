# -*- coding:utf-8 -*-
from scapy.all import *
from random import randint
import sys

from scapy.layers.inet import ICMP, IP
from scapy.layers.l2 import Ether

send(IP(dst="192.168.18.193") / ICMP())
