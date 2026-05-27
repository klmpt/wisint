import socket

def quick_scan(ip):
    print(f"[*] fast scan for: {ip}")
    open_ports = []
    for port in [21, 22, 80, 443, 3306]:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        if s.connect_ex((ip, port)) == 0:
            open_ports.append(port)
        s.close()
    return open_ports