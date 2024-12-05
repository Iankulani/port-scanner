# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 20:39:25 2024

@author: IAN CARTER KULANI

"""
import socket

def scan_port(ip, port):
    """Scan a single port on the given IP address."""
    try:
        # Create a socket object
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Set a timeout for the connection attempt
        sock.settimeout(1)
        # Attempt to connect to the specified IP and port
        result = sock.connect_ex((ip, port))
        # Check if the port is open
        if result == 0:
            print(f"Port {port} is open on {ip}.")
        else:
            print(f"Port {port} is closed on {ip}.")
    except socket.error as err:
        print(f"Error connecting to {ip}:{port} - {err}")
    finally:
        sock.close()

def main():
    print("================port scanner================\n")
    # Input the target IP address and port range
    target_ip = input("Enter the IP address to scan:")
    start_port = int(input("Enter the starting port number:"))
    end_port = int(input("Enter the ending port number:"))

    # Scan the specified range of ports
    for port in range(start_port, end_port + 1):
        scan_port(target_ip, port)

if __name__ == "__main__":
    main()