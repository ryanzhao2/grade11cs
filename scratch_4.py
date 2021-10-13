import random

low_value = int(input("Enter a low value"))
high_value = int(input("Enter a high value"))
your = str("Your number is: ")
randomvalue = random.randint(low_value, high_value)
print(f'{your}{randomvalue}')