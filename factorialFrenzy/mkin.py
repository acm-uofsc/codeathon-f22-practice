#!/usr/local/bin/python3
from random import randint
case_num = int(input())
# 0 and 1 are the sample cases
if case_num == 0:
    print(0)
elif case_num == 1:
    print(1)
elif case_num == 2:
    print(3)
else:
    # output what should be read in as input by
    # contestant code
    n = randint(0, int(1e4))
    print(n)
