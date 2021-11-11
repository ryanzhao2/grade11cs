#RYAN ZHAO
#October 15, 2021
#QUESTION #1

def compare(x, y):
    if x < y:
        print(f'{x} is less than {y}')

    elif x > y:
        print(f'{x} is greater than {y}')

    else:
        print(f' {x} and {y} are equal')

#MAIN
num_1 = float(input("Enter a number: "))
num_2 = float(input("Enter another number: "))
compare(num_1, num_2)
