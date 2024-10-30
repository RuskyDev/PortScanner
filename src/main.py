import os
import socket
import threading
import sys
from colorama import Fore, init
import fade
init()

def Scan(target_ip, port, open_ports):
    tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_sock.settimeout(1)

    udp_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_sock.settimeout(1)

    try:
        tcp_sock.connect((target_ip, port))
        open_ports.append((port, 'TCP'))
        print(f"    {Fore.WHITE}[{Fore.GREEN}INFO{Fore.WHITE}] Port :{Fore.YELLOW}{port}{Fore.WHITE} (TCP) is open")
    except (socket.timeout, socket.error):
        pass
    finally:
        tcp_sock.close()

    try:
        udp_sock.sendto(b'', (target_ip, port))
        data, _ = udp_sock.recvfrom(1024)
        open_ports.append((port, 'UDP'))
        print(f"    {Fore.WHITE}[{Fore.GREEN}INFO{Fore.WHITE}] Port :{Fore.YELLOW}{port}{Fore.WHITE} (UDP) is open")
    except (socket.timeout, socket.error):
        pass
    finally:
        udp_sock.close()

def ParseArgs(args):
    target_ip, start_port, end_port = None, None, None
    for arg in args:
        if arg.startswith("--target-ip="):
            target_ip = arg.split("=")[1]
        elif arg.startswith("--start-port="):
            start_port = int(arg.split("=")[1])
        elif arg.startswith("--end-port="):
            end_port = int(arg.split("=")[1])

    if not target_ip or start_port is None or end_port is None:
        print("Usage: script.py --target-ip=<IP> --start-port=<start> --end-port=<end>")
        sys.exit(1)

    if not (0 <= start_port <= 65535) or not (0 <= end_port <= 65535):
        print("Error: Ports must be in the range 0-65535.")
        sys.exit(1)

    return target_ip, start_port, end_port

if __name__ == "__main__":
    target_ip, start_port, end_port = ParseArgs(sys.argv[1:])
    os.system("cls" if os.name == "nt" else "clear")
    logo = fade.brazil(""" 
    ██████╗  ██████╗ ██████╗ ████████╗███████╗ ██████╗ █████╗ ███╗   ██╗███╗   ██╗███████╗██████╗ 
    ██╔══██╗██╔═══██╗██╔══██╗╚══██╔══╝██╔════╝██╔════╝██╔══██╗████╗  ██║████╗  ██║██╔════╝██╔══██╗
    ██████╔╝██║   ██║██████╔╝   ██║   ███████╗██║     ███████║██╔██╗ ██║██╔██╗ ██║█████╗  ██████╔╝
    ██╔═══╝ ██║   ██║██╔══██╗   ██║   ╚════██║██║     ██╔══██║██║╚██╗██║██║╚██╗██║██╔══╝  ██╔══██╗
    ██║     ╚██████╔╝██║  ██║   ██║   ███████║╚██████╗██║  ██║██║ ╚████║██║ ╚████║███████╗██║  ██║
    ╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝
    """)
    print(logo)
    print("    This was made for educational purposes only. Only scan ports on devices you have permission to access.")
    print()
    print(f"    {Fore.WHITE}[{Fore.GREEN}INFO{Fore.WHITE}] Scanning ports on {Fore.YELLOW}{target_ip}{Fore.WHITE}\n")

    open_ports = []
    ports_range = range(start_port, end_port + 1)
    threads = []

    for port in ports_range:
        thread = threading.Thread(target=Scan, args=(target_ip, port, open_ports))
        thread.start()
        threads.append(thread)
        if len(threads) >= 100:
            threads = [t for t in threads if t.is_alive()]

    [thread.join() for thread in threads]

    if open_ports:
        open_ports_str = "\n".join([f"{port} ({proto})" for port, proto in open_ports])
        with open("open-ports.txt", "w") as file:
            file.write(open_ports_str)
    else:
        print(f"    {Fore.WHITE}[{Fore.RED}ERROR{Fore.WHITE}] No ports are open")

    print(f"    {Fore.WHITE}[{Fore.GREEN}INFO{Fore.WHITE}] Port scanning is complete, and open ports have been saved in {Fore.YELLOW}./open-ports.txt{Fore.WHITE}.")
    print(f'    {Fore.WHITE}[{Fore.GREEN}INFO{Fore.WHITE}] Press any key to close the Port Scanner, or type "exit".')
    input()
    exit()
