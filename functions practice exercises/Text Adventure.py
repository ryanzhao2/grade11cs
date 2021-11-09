import textwrap
bold = "\033[1m"
reset_bold = "\033[0m"
new_line = "\n" * 20

def start():
    print(bold + "Welcome to Squid Game" + reset_bold)
    start = input("Enter 1 to start: ")

    if start == '1':
        home()
    print('Invalid Answer')



def home():

    text_home = bold + "\nYou recently lost your job and a hard time living with the little money available,\
and also owe people some money." + reset_bold
    print(textwrap.fill(text=text_home, width=80, replace_whitespace=False))
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
    text_job = bold + "\nYou forgot to wake up early the day of the interview, and arrive an hour late and fail the interview." + reset_bold
    print(textwrap.fill(text=text_job, width=80, replace_whitespace=False))
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
    text_casino = bold + "\nYou start making money, however get greedy and lose it all in the end." + reset_bold
    print(textwrap.fill(text=text_casino, width=80, replace_whitespace=False))
    print("1 - Walk to the train station to go home")

    option = input("Enter 1 to continue: ")
    if option == '1':
        train_station()
    print('Invalid Answer')

def train_station():
    text_train_station = bold + "\nYou arrive at the train station and someone offers you to play a game to win some money,\
 and eventually you make some money from the game. He then passes a card to you with a number\
 on it and tells you to call it to make a lot more money." + reset_bold
    print(textwrap.fill(text=text_train_station, width=80, replace_whitespace=False))
    print("Make a decision")
    print("1 - Call the number and accept the offer.")
    print("2 - Ignore the card, and buy lunch with the money. ")
    option = input("Enter your choice: ")
    if option == '1':
        van()
    elif option == '2':
        financial()
    print('Invalid Answer')

def financial():
    text_financial = bold + "One week has passed, and poor financial decisions have led to you losing all the money. \
    However, you still have the card." + reset_bold
    print(textwrap.fill(text=text_financial, width=80, replace_whitespace=False))
    print("Make a decision")
    print("1 - Throw out the card and find a new job")
    print("2 - Call the number and accept the offer.")
    option = input("Enter your choice: ")
    if option == '1':
        homeless()
    elif option == '2':
        van()
    print('Invalid Answer')

def homeless():
    text_homeless = bold + "You Lose\nafter a couple days, you quickly realize that you have no chance of \
    getting a job with the poor living conditions you're in and live the rest of your life homeless " + reset_bold
    print(textwrap.fill(text=text_homeless, width=80, replace_whitespace=False))
    option = input("Enter 1 to restart")
    if option == '1':
        home()
    print('Invalid Answer')

def van():
    text_van = bold + "\nYou get picked up in a van and wake up in a facility with hundreds of other people. \
The people running the facility announces that there will be 6 games played over 6 days with a grand prize of 36 million USD." + reset_bold
    print(textwrap.fill(text=text_van, width=80, replace_whitespace=False))
    print("Make a decision")
    print("1 - Try to form an alliance ")
    print("2 - Sit alone and ignore others")
    option = input("Enter your choice: ")
    if option == '1':
        #friends = True
        #return friends
        first_game()
    if option == '2':
        #friends = False
        #return friends
        first_game()

def first_game():
    text_first_game = bold + "\nThe first game is announced and it is red light, green light. However, \
you have only 5 minutes to get across the line." + reset_bold
    print(textwrap.fill(text=text_first_game, width=80, replace_whitespace=False))
    print("Make a decision")
    print("1 - Take your time and watch your step ")
    print("2 - Stand behind people to hide movement and move at a comfortable pace.")
    print("3 - Run and try to get across quickly")
    option = input("Enter your choice: ")
    if option == '1':
        lose_slow()
    if option == '2':
        first_win()
    if option == '3':
        lose_fast()

def lose_slow():
    text_lose_slow = bold + "\nYou Lose\nThe timer runs out you get shot after only making it past halfway." + reset_bold
    print(textwrap.fill(text=text_lose_slow, width=80, replace_whitespace=False))
    option = input("Enter 1 to restart")
    if option == '1':
        home()
    print('Invalid Answer')

def lose_fast():
    text_lose_fast = bold + "\nYou Lose\nYou run at a quick pace and almost make it to the finish line,\
however you trip and get shot." + reset_bold
    print(textwrap.fill(text=text_lose_fast, width=80, replace_whitespace=False))
    option = input("Enter 1 to restart")
    if option == '1':
        home()
    print('Invalid Answer')

def first_win():
    text_first_win = bold + "\nYou barely get across with only 20 seconds left on the timer and\
then head back to the main room " + reset_bold
    print(textwrap.fill(text=text_first_win, width=80, replace_whitespace=False))
    option = input("Enter 1 to get a good nights sleep: ")
    if option == '1':
        second_game()
    print('Invalid Answer')


def second_game():
    text_second_game = bold + "\nThe hosts have now brought everyone to play a new game in an indoor playground.\
In front of you, there are four shapes to choose from."
    print(textwrap.fill(text=text_second_game, width=80, replace_whitespace=False))
    print("1 - \u25B3")
    print("2 - \u2602")
    print("3 - \u2299")
    print("4 - \u2605")
    option = input("Choose a shape: ")

def third_game():
    pass

def fourth_game():
    pass

def fifth_game():
    pass

def sixth_game():
    pass
start()