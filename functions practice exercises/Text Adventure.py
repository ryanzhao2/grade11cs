def start():
    print("Welcome to Squid Game")
    start = input("Enter 1 to start: ")

    if start == '1':
        home()
    print('Invalid Answer')


def home():
    print("\nYou recently lost your job and a hard time living with the little money available, and also owe people some money.")
    print("Make a decision")
    print("1 - Apply for a job")
    print("2 - Gamble the rest of the money you have at a casino")

    option = input("Enter your choice: ")

    if option == '1':
        job()
    elif option == '2':
        casino()
    print('Invalid Answer')



def job():
    print("\nYou forgot to wake up early the day of the interview, and arrive an hour late and fail the interview.")
    print("Make a decision")
    print("1- Gamble the rest of the money you have at a casino")
    print("2- Walk to the train station to go home")

    option = input("Enter your choice: ")
    if option == '1':
        casino()
    elif option == '2':
        train_station()
    print('Invalid Answer')

def casino():
    print("\nYou start making money, however get greedy and lose it all in the end.")
    print("1 - Walk to the train station to go home")

    option = input("Enter 1 to continue: ")
    if option == '1':
        train_station()
    print('Invalid Answer')

def train_station():
    print("You arrive at the train station and someone offers you to play a game to win some money,\n
          and eventually you make some money from the game He then passes a card to you with a number \n
          on it and tells you to call it to make a lot more money.")
    print("1 - Call the number and accept the offer.")
    print("2 - Ignore the card, and buy lunch with the money. ")
    option = input("Enter your choice: ")
    if option == '1':
        first_game()
    elif option == '2':
        second_game()
    print('Invalid Answer')

def first_game():
    pass

def second_game():
    pass

def third_game():
    pass

def fourth_game():
    pass

def fifth_game():
    pass

def sixth_game():
    pass
start()