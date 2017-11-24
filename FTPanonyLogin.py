#!/usr/bin/python

import socket
import re
import sys
from colorama import init
init(strip=not sys.stdout.isatty())
from termcolor import cprint
from pyfiglet import figlet_format

if len(sys.argv) <= 2:
	print("\n USO: python ftpdefaul.py ips.txt anonymous anonymous\n")
	sys.exit(0)
else:
	cprint(figlet_format('Tux_1337', font='starwars'),
	'yellow','on_blue', attrs=['bold'])
	b = '''	[+][+][+][+][+][+][+][+][+][+][+]
	[+]   CODED by: Tux_1337      [+]
	[+]   TELEGRAM: @C4P40        [+]
	[+]      \{+_+}/              [+]
	[+][+][+][+][+][+][+][+][+][+][+]\n\n'''
	print b
file = open(sys.argv[1])
for ip in file.readlines():
	soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	soc.connect((ip,21))
	banner = soc.recv(1024)
	soc.send("USER "+sys.argv[2]+"\r\n")
	banner = soc.recv(1024)
	soc.send("PASS "+sys.argv[3]+"\r\n")
	banner = soc.recv(1024)
	if re.search('230',banner):
		print " [+] CONTA DEFAULT NO IP: "+ip+banner+"\r\n"
