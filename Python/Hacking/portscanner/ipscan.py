import portscanner

ip = '127.0.0.1, 192.168.8.1'


if ',' in ip:
    for ip_add in ip.split(','):
        portscanner.scan(ip_add.strip(' '))
else:
    portscanner.scan(ip)
