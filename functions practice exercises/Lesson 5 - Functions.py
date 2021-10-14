
#QUESTION #6
"""
def boxname(name):
    s = '*' * (len(name) + 2) + '\n'
    s += f'*{name}*\n'
    s += '*' * (len(name) + 2) + '\n'
    return s

name = input("Enter your name")


print(boxname(name))
"""

#QUESTION #7
"""
def clear_screen():
    for i in range(25):
        print('\n')
clear_screen()
"""

#QUESTION #8
"""def is_leap_year(some_year):
    if (some_year % 4 == 0 and some_year % 100 != 0 or some_year % 400 == 0):
        return True
    return False


user_year = int(input("Enter a number: "))
print(is_leap_year(user_year))
"""