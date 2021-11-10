"""
from time import sleep

def slow_print(s):

    for i in range(len(s)):
        print(s[i],end="")
        sleep(1/8)

slow_print("This is a test")
"""


def total(a,b):
    sum=a+b
    if sum <= 19 and sum >= 10:
        return 20
    else:
        return sum

amount = total(30, 10)
print(f'{amount}')