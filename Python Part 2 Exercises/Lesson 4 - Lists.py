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
    avg = sum(some_list) / len(some_list)
    return avg

#main
list = [1, 2, 3, 4, 5]
print(list_average(list))
"""

#QUESTION #6
"""
people = ['Rema Wilkin', 'Kiyoko Sandor', 'Heriberto Cruikshank', 'Demetria Novoa', 'Clelia Necessary', 'Mahalia Spadaro', 'Barry Ager', 'Collin Blanche', 'Pearline Sokoloff', 'Garland Hedgecock', 'Nicola Deltoro', 'Shaniqua Mendelson', 'Kris Bucy', 'Rashida Koester', 'Elane Sweetser', 'Estela Lawley', 'Micki Brass', 'Emmanuel Tufts', 'Lenita Michalec', 'Ha Mcelhannon', 'Domonique Sutera', 'Hoyt Camden', 'Arlyne Messenger', 'Dagmar Berra', 'Gregoria Belmont', 'Sylvie Guyette', 'Gaston Christianson', 'Lora Holleman', 'Lesley Leininger', 'Paige Nolen']

print(f'{"Lastname,":<15} {"Firstname":<15}')
print("-"*31)

for name in people:
    s = name.split()
    print(f'{s[1]:<15} {s[0]:<20}')
"""

#QUESTION #7
"""
def list_greater_smaller(some_list):
    count_greater50 = 0
    count_less50 = 0
    for char in some_list:
        if char > 50:
            count_greater50 += 1
        if char < 50:
            count_less50 += 1
    return [count_greater50, count_less50]


# MAIN
your_random_list = [5, 52, 48, 30, 80, 100, 4, 76]
both_counts = list_greater_smaller(your_random_list)
print(both_counts)
"""

#QUESTION #8
"""
#IN THIS EXAMPLE, i is iterating through the list so it takes on the values of the cities
cities = ['Badalona', 'Calama', 'Dadu', 'Enshi', 'Kano', 'Haldia', 'Passos']

# example 1
for item in cities:
    print(f'{item:<12} and variable i is datatype {type(item)}')

print("\n\n")

#In this example, i is iterating through the indices of the list and goes through 1 to the last value so it takes on index values(numbers) instead of the cities
# example 2
for index in range(0, len(cities)):
    print(f'{index:<2} {cities[index]:<12} and variable i is datatype {type(index)}')
#These variable names are better choices because they are more descriptive and represent what they do more clearly and accurately as one is displaying the cities and the other is displaying the indices
"""

#QUESTION #9
"""
list = []
user_input = input("Please enter an item to add to list, type 'end' to complete: ")

while user_input != 'end':
    list.append(user_input)
    user_input = input("Please enter an item to add to list, type 'end' to complete: ")

list.sort()
print(list)
"""

#QUESTION #10
"""
def getMonthName(monthNum):
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    for i in range(12):
        if i+1 == monthNum:
            return months[i]



m = int(input("Please enter the month number"))
print(getMonthName(m))
"""

#QUESTION #11
"""
zoo_1 = ['bengal tiger', 'caspian tiger', 'siberean tiger', 'south china tiger', 'indochinese tiger', 'lion', 'jaguar', 'cougar', 'leopard', 'snow leopard', 'cheetah', 'clouded leopard']
zoo_2 = ['siberean tiger', 'south china tiger', 'lion', 'snow leopard', 'clouded leopard']

unique_species = []

for animal in zoo_1:
    for animal2 in zoo_2:
        if animal == animal2:
            unique_species.append(animal)
print(unique_species)
"""

#QUESTION #12
"""
import random


def generate_characters(quantity):
    lastnames = ['Wilson',
                 'Peralta',
                 'McCaffrey',
                 'Betts',
                 'Willis',
                 'Ewing',
                 'Franklin',
                 'Carey',
                 'Parra',
                 'Walters',
                 'Beck',
                 'Cole',
                 'Armstrong',
                 'Stone',
                 'Henderson',
                 'Harrison',
                 'Dixon',
                 'Brady',
                 'Jimenez', 'Fitzgerald']
    firstnames = ['Todd',
                  'Nicholas',
                  'Teresa',
                  'Jennifer',
                  'Gloria',
                  'Bobby',
                  'Angela',
                  'Justin',
                  'Kimberly',
                  'Arthur',
                  'John',
                  'Johnny',
                  'Carol',
                  'Brian',
                  'Heather',
                  'Jason',
                  'Daniel',
                  'Norma',
                  'Eric',
                  'Douglas',
                  'Paula',
                  'Larry',
                  'Eugene',
                  'Ruth', 'Betty']
    ages = [30, 40, 35, 42, 38, 51, 58, 46, 36]
    cities = ['Fez', 'Budapest', 'Rome', 'Hong Kong', 'Mexico City', 'Milan', 'Philadelphia', 'Dallas', 'Sana\'a']
    occupation = ['Architect', 'Librarian', 'Illustrator', 'Landscape gardner', 'Bank clerk', 'Au pair',
                  'Legal secretary', 'Property developer', 'Publisher']

    characters = []

    for i in range(0, quantity):
        c = f'{random.choice(lastnames)}, {random.choice(firstnames)}, {str(random.choice(ages))}, {random.choice(cities)}, {random.choice(occupation)}'
        characters.append(c)

    return characters



def print_characters(aList):
    print("Characters in list are")
    print("-" * 30)
    for i in range(0, len(aList)):
        print(f'{i + 1:>3}. {aList[i]}')


# main
number_characters = int(input("How many random characters do you wish to generate?"))

list_characters = generate_characters(number_characters)

print_characters(list_characters)
"""