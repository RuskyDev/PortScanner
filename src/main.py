import os
import socket
import threading
import json
from colorama import Fore, init
init()

def scan_port(target_ip, port, open_ports):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)

    try:
        sock.connect((target_ip, port))
        open_ports.append(port)
        print(f"{Fore.WHITE}[{Fore.LIGHTGREEN_EX}OPEN{Fore.WHITE}] Port {Fore.YELLOW}:{port}{Fore.WHITE} is open")
    except (socket.timeout, socket.error):
        pass
    finally:
        sock.close()

def write_to_file(file_path, content):
    with open(file_path, "w") as file:
        file.write(content)

if __name__ == "__main__":
    with open("config.json", "r") as config_file:
        config = json.load(config_file)

    target_ip = config.get("target_ip", "127.0.0.1")
    os.system("cls" if os.name == "nt" else "clear")

    print(f"{Fore.WHITE}[{Fore.GREEN}INFO{Fore.WHITE}] Scanning ports on {Fore.YELLOW}{target_ip}{Fore.WHITE}\n")

    start_port = config.get("start_port", 1)
    end_port = config.get("end_port", 65535)

    open_ports = []

    threads = [threading.Thread(target=scan_port, args=(target_ip, port, open_ports)) for port in range(start_port, end_port + 1)]
    [thread.start() for thread in threads]
    [thread.join() for thread in threads]

    if open_ports:
        open_ports_str = "\n".join(map(str, open_ports))
        write_to_file("open_ports.txt", open_ports_str)
    else:
        print(f"{Fore.WHITE}[{Fore.LIGHTRED_EX}ERROR{Fore.WHITE}] No ports are open")

    print(f"{Fore.WHITE}[{Fore.GREEN}INFO{Fore.WHITE}] Port scanning is complete.")
    print(f'{Fore.WHITE}[{Fore.GREEN}INFO{Fore.WHITE}] Press any key to close the Port Scanner, or type "exit".')
    input()
    exit()
