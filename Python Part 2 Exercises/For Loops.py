#QUESTION #1
#example 1
"""
for i in range(0, 50, 10):
     print(i)
#prints(0, 10, 20, 30, 40 with new lines between each number)

#example 2
for i in range(1, 21):
     print(f'{i}. "Hello World!"')
#prints loops it 20 times and prints the number and "Hello World!" each time

#example 3
for i in range(0, 10):
     for j in range(0, 5):
          print(f'{i} - {j}: The Matrix')
#loops 50 times and prints i - j and "The Matrix"

#example 4
n = 10
for j in range(1, 11):
     print(j * n)
     n = n - 1
#loops j 10 times and prints every time it loops to multiply with n. Then subtracts n by 1.

#example 5
count = 0
for d in range(7):
   for h in range(24):
      for m in range(60):
         for s in range(60):
            count += 1
print(count)

#look up how many seconds one week has
"""

#QUESTION 2
"""
for i in range(5, 1001, 5):
     print(i)
"""
"""
#QUESTION 3
def print_times_table(table_number):
     count = 1
     for i in range(1, 101):
          print(f'{i} * {table_number} = {count * table_number}')
          count += 1






times_table_num = int(input("Enter the times table you'd like to see: "))
print_times_table(times_table_num)
"""
#QUESTION 4

def print_temperature_table():
     print("Celcius to Fahrenheit Table\n---------------------------")
     for C in range(-20, 36, 5):
          F = int(C * 9 / 5 + 32)
          print(f'{C: >3} C --> {F: >3} F')



#MAIN
print_temperature_table()
