#!/usr/bin/env python
import os

temp = os.popen("vcgencmd measure_temp").readline()
print(temp)

