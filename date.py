#!/usr/bin/python3
import subprocess
print("content-type: text/html")
print()


x=subprocess.getoutput("date")
print(x)

