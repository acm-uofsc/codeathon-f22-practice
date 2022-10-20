#!/usr/local/bin/python3
from random import choices, randint
from string import ascii_letters
case_num = int(input())
# 0 and 1 are the sample cases
if case_num == 0:
    print('Hera sucks')
elif case_num == 1:
    print('I\'m bad at programming')
else:
    # output what should be read in as input by
    # contestant code
    n = randint(1, 100)
    print(*choices(ascii_letters, k=n), sep='')
