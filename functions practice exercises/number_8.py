def is_leap_year(some_year):
    if (some_year % 4 == 0 and some_year % 100 != 0 or some_year % 400 == 0):
        return True
    return False


user_year = int(input("Enter a number: "))
print(is_leap_year(user_year))

"""
def my_leap_year (year):
    if(year % 100 == 0 and year %400 != 0):
        return False
    elif (year % 4 == 0 or year % 400 == 0):
        return True
    return False

print(my_leap_year(user_year))
"""