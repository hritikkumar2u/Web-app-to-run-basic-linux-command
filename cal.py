#!/usr/bin/python3

import subprocess

print("content-type: text/html")
print()

x=subprocess.getoutput("cal")
print(x)
