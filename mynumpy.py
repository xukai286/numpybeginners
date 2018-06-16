from __future__ import print_function
import sys
from datetime import datetime

import numpy as np


"""
    备注
"""


def numpynum(n):
    a = np.arange(n) ** 2
    b = np.arange(n) ** 3
    c = a + b
    return c

def pythonsum(n):
    a = range(n)
    b = range(n)
    # a = [0,1,2,3]
    # b = [0,1,2,3]
    c = []

    for i in range(len(a)):
        # a[i] = i ** 2
        # b[i] = i ** 3
        # print(a[i])
        c.append(i**2 + i**3)
    return c

size = int(sys.argv[1])
print("the size is",size)
start = datetime.now()
c = pythonsum(size)
delta = datetime.now() - start
print("The last 2 elements of the sum",c[-2:])
print("PythonSum elapsed time in microsecond ", delta.microseconds)

start = datetime.now()
print("the size is",size)
c = numpynum(size)
delta = datetime.now() - start
print("The last 2 elements of the sum",c[-2:])
print("Numpynum elapsed time in microsecond ", delta.microseconds)


# print(numpynum(5))
