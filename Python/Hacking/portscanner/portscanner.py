import socket
import sys
from IPy import IP


def scan(target):
    converted_ip = check_ip(target)
    print('\n' + '[-_0 Scanning Target] ' + str(target))

    for port in range(fport, lport):
        scan_port(converted_ip, port)


def check_ip(ip):
    try:
        IP(ip)
        return(ip)
    except ValueError:
        return socket.gethostbyname(ip)  # Converts Domain into IP


def get_banner(sock):
    return sock.recv(1024)


def scan_port(ipaddress, port):
    try:
        s = socket.socket()
        s.settimeout(0.5)
        s.connect((ipaddress, port))
        try:
            banner = get_banner(s)
            print('[+] Open Port ' + str(port) +
                  ' : ' + str(banner.decode.strip('\n')))
        except:
            print('[+] Open Port ' + str(port))
    except:
        pass


if __name__ == '__main__':
    targets = input(
        '[+] Enter Target/s To Scan(split multiple targets with,): ')

    while 1:
        try:
            fport = int(input('Enter First Ports That you Want To Scan: '))
            lport = int(input('Enter Last Ports That you Want To Scan: ')) + 1
            break
        except ValueError:
            print('Your Input needs to be and Integer')

    if ',' in targets:
        for ip_add in targets.split(','):
            scan(ip_add.strip(' '))
    else:
        scan(targets)
else:
    fport = int(1)
    lport = int(500)
