#!/usr/bin/env python3
import platform
import os
import datetime
import time

SAFE_HOSTS = {
# add more entries here:
#
#
    "Google DNS": "8.8.8.8",
    "Cloudflare DNS": "1.1.1.1"
}

def ping_host(ip):
    current_os = platform.system().lower()

    if current_os == "linux":
        cmd = f"ping -c 1 -w 2 {ip} > /dev/null 2>&1"
    elif current_os == "windows":
        cmd = f"ping -n 1 -w 2 {ip} > nul"
    else:
        raise OSError(f"Unsupported OS: {current_os}")

    return os.system(cmd)

def check_network_health():
    for name, ip in SAFE_HOSTS.items():
        result = ping_host(ip)
        status = "REACHABLE" if result == 0 else "UNREACHABLE"
        print(f"({ip}): {status}")

while True:
    check_network_health()
    time.sleep(5)  # checks every 5 secs
