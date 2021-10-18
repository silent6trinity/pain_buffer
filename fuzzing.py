#!/usr/bin/python

#TODO: Change this to python3, because we're not barbarians
import time, struct, sys
import socket as so


# Create an array of buffers, from 1 to 1000 elements, with increments of 200 bytes each.
buff=["A"]
# max number of buffers in the array
max_buffer = 1000
# initial value of the counter
counter=100
# increment value
increment=200

while len(buff) <= max_buffer:
    buff.append("A"*counter)
    counter=counter+increment

for string in buff:
    try:
        server = sys.argv[1]
        port = sys.argv[2]
    except IndexError:
        print "[+] Usage %s host + port " % sys.argv[0]
        sys.exit()

    print "Fuzzing with %s bytes" % len(string)
    s = so.socket(so.AF_INET, so.SOCK_STREAM)
    try:
        s.connect((server, port))
        print s.recv(1024)
        s.send( string+'\r\n')
        s.send('exit\r\n')
        print s.recv(1024)
    except:
        print "[!] connection refused, check debugger"
        sys(exit)
