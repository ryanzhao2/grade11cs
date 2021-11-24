#QUESTION #1
"""
list_numbers = [5, 6, 3, 2, 54, 32, 23, 12, 21, 75, 43, 1]
max_in_list = max(list_numbers)
min_in_list = min(list_numbers)
print(max_in_list)
print(min_in_list) #Printed the number 1
"""

#QUESTION #2
"""
import random

def make_random_list(quantity):

     random_numbers = [ ]

     for i in range(quantity):
         random_numbers.append(random.randrange(100))
     return random_numbers


#MAIN
result = make_random_list(50)
print(result)
"""

#QUESTION #3
"""
import random

def make_random_list(quantity):

     random_numbers = [ ]

     for i in range(quantity):
         random_numbers.insert(0, random.randrange(100))
     return random_numbers


#MAIN
result = make_random_list(50)
print(result)
"""

#QUESION #4
"""
#Replicates the .pop function
def someListFunction( a, i):
      temp = a[i]
      for j in range(i, len(a) - 1):
         a[j] = a[j + 1]

      del a[len(a) - 1]

      return temp

print(someListFunction('h21321i2131231231', 1))
"""

#QUESTION #5
"""
def list_average(some_list):


   return avg
"""
#main