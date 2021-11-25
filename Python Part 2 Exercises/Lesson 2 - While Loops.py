#QUESTION #1
"""
continue_repeat = "end"

while(continue_repeat == "end"):
    print("Have a good day")
"""

#QUESTION #2
"""
user_input = input("Type more to continue: ")

while (user_input == "more"):

        print("Have a good day.")

else:
        print("Done")
"""

#QUESTION #3
"""
user_input = "more"
count = 0
while (user_input == "more"):
        print("Have a good day.")
        user_input = input("Type more to continue: ")
        count += 1

print("Done")
print(count)
"""

#QUESTION #4
"""
#THIS CODE DOESNT INCLUDE 0 AS A NUMBER THAT'S INCLUDED IN THE AVERAGE BUT JUST AS AN INDICATION THAT THEY ARE DONE
#IF YOU WANT TO INCLUDE 0 IN THE AVERAGE, REMOVE THE IF CONDITION
total_sum = 0
number_of_numbers = 0
user_input = ""
while (user_input != 0):
    user_input = int(input("Enter a number"))
    total_sum += user_input
    number_of_numbers += 1
if user_input == 0:
    number_of_numbers -= 1

print(total_sum / number_of_numbers)
"""

#QUESTION #5
"""
count = 0
qqq_stock = 25.23
annual_growth_rate = 0.163
goal_value = 100

while qqq_stock < 100:
    qqq_stock = qqq_stock * (1 + annual_growth_rate)
    count += 1
print(count)
"""
#QUESTION #6
"""
for num in range(20):
    print(f'{num:>3} X 5 = {num * 5}')
    num = num + 1
"""

#QUESTION #7
"""
import random
count = 0
sum = 0
while sum < 100:
    number = random.randint(1, 6)
    sum += number
    count += 1
    print(f'rolled a {number} >>> total is {sum}')
print(f'total number of roles is {count}')
"""


#QUESTION #8
"""
import random
count = 0
sum = 0
while sum < 100:
    first = random.randint(1, 6)
    sum += first
    second = random.randint(1, 6)
    sum += second
    print(f'rolled a {first} and a {second} >>> total is {sum}')
print(f'total number of roles is {count}')
"""

#QUESTION #9
"""
import random
count = 0
roll = ""
first = random.randint(1, 6)
print(f'Your first roll is {first}')
while roll != first:
    roll = random.randint(1, 6)
    print(f'rolled a {roll}')
    count += 1
print(f'It took {count} rolls to reach your point of {first} again')
"""

#QUESTION #10
"""
import random

computer = random.randint(1, 100)
user_input = int(input("Enter a number"))
while user_input < computer:
    print('higher')
    user_input = int(input("Enter a number"))

while user_input > computer:
    print('lower')
    user_input = int(input("Enter a number"))

print("That's correct")
"""

#QUESTION #11
"""
import random
computer = random.randint(1, 20)
computer_2 = random.randint(1, 20)
sum = computer + computer_2

user_input = int(input(f'{computer} + {computer_2} = ???'))

while user_input != sum:
    user_input = int(input(f'{computer} + {computer_2} = ???'))

print(f'You got it right! {computer} + {computer_2} = {sum}')
"""