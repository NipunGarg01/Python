#!usr/bin/python
import telnetlib
HOST="10.184.96.161"
tn= telnetlib.Telnet ( HOST,8888,2)
tn.read_until (b"--->", 2)
tn.write(b"se on\n")
tn.read_until (b"Password:", 2)
tn.write (b"secret\n")
tn.read_until(b"--->",2)
tn.write(b"rs 7\n")
tn.read_until (b"bash-4.3#",2)
tn.write(b"saos\n")
f=tn.read_until(b">",2)
print (f)



