#!/usr/bin/env python

temp = os.popen("vcgencmd measure_temp").readline()
print(temp)

