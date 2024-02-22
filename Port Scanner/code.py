#!/bin/python
import sys
import socket
from datetime import datetime

target = input("Please enter the IP you want to scan: ")
if not target:
    print("Input is blank. Exiting program.")
    print("Please enter domain name or ip address!!!")
    sys.exit()
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])  # Translate hostname to IPV4
else:
    print("")

# Ending Banner
print("-" * 50)
print("Scanning target " + target)
print("Time started: " + str(datetime.now()))
print("-" * 50)
print("")

for port in range(1, 65536):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    result = s.connect_ex((target, port))
    if result == 0:
        try:
            print(
                "Port {} Open Found |  Service Running: {}".format(
                    port, socket.getservbyport(port, "tcp")
                )
            )
        except socket.error:
            print("Port {} Close Found |  Service Running: {}".format(port, "Unknown"))
# Closing Banner
print("")
print("-" * 50)
print(target + " scanning is complete")
print("Finished at: " + str(datetime.now()))
print("-" * 50)
