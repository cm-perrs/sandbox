#!/usr/bin/env python
import os

filename = "address.txt"
lines = tuple(open(filename, 'r'))
temp = os.popen("vcgencmd measure_temp").readline()
print(temp)

