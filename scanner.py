# scrapy for network scanning and analysis
# paramiko for SSH connection and running commands
# pandas for data analysis and report generation

import scapy
from scapy.all import *
import paramiko
import pandas as pd

target_ip = ''
target_ports = []

def scanner(ip, ports) :
    print("working")