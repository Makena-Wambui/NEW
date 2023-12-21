#!/usr/bin/python3
from datetime import datetime
today = datetime.now()
str_s = str(today)
print(str_s)
# eval(str_s)
repr_s = repr(today)
print(repr_s)
# eval(repr_s) returns a datetime.datetime object
# time = eval(repr_s)
# print(type(time))
