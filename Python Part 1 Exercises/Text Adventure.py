import textwrap
import random
from time import sleep

bold = "\033[1m"
reset_bold = "\033[0m"
new_line = "\n" * 20
short_line = "\n" * 3
good_shape = True
players = ['young woman', 'middle-aged woman', 'old man', 'middle-aged man',\
           'body builder', 'teenager', 'middle-aged man', 'old lady', 'intelligent man','young woman']

from time import sleep


def slow_print(s, line_length):
    line_end = False

    for i in range(len(s)):
        if (i + 1) % line_length == 0 and i > 0:
            line_end = True
        if line_end and (s[i] == " " or s[i] == "\n"):
            print("")
            line_end = False
        else:
            print(s[i], end="")
        sleep(1 / 20)

def start():
    slow_print(bold + "Welcome to Squid Game\n" + reset_bold, 80)
    input("Press Enter to Continue: ")

    home()

def home():
    slow_print(bold + "\nYou recently lost your job and have a hard time living with the little money available,\
 and also owe people some money.\n" + reset_bold, 80)
    print("1 - Apply for a job")
    print("2 - Gamble the rest of the money you have at a casino")
    option = input("Enter your choice: ")

    while not(option == '1' or option == '2'):
        option = input("Invalid Answer. Enter your choice again(1 or 2): ")
    if option == '1':
        job()
    elif option == '2':
        casino()

def job():
    text_job = bold + "\nYou forgot to wake up early the day of the interview, and arrive an hour late and fail the interview." + reset_bold
    print(textwrap.fill(text=text_job, width=80, replace_whitespace=False))
    print("Make a decision")
    print("1- Gamble the rest of the money you have at a casino")
    print("2- Walk to the train station to go home")

    option = input("Enter your choice: ")
    while not(option == '1' or option == '2'):
        option = input("Invalid Answer. Enter your choice again(1 or 2): ")
    if option == '1':
        casino()
    elif option == '2':
        train_station()


def casino():
    text_casino = bold + "\nYou start making money, however get greedy and lose it all in the end." + reset_bold
    print(textwrap.fill(text=text_casino, width=80, replace_whitespace=False))
    print("1 - Walk to the train station to go home")

    input("Press Enter to Continue: ")
    train_station()


def train_station():
    text_train_station = bold + "\nYou arrive at the train station and someone offers you to play a game to win some money,\
 and eventually you make some money from the game. He then passes a card to you with a number\
 on it and tells you to call it to make a lot more money." + reset_bold
    print(textwrap.fill(text=text_train_station, width=80, replace_whitespace=False))
    print("Make a decision")
    print("1 - Call the number and accept the offer.")
    print("2 - Ignore the card, and buy lunch with the money. ")
    option = input("Enter your choice: ")
    while not(option == '1' or option == '2'):
        option = input("Invalid Answer. Enter your choice again(1 or 2): ")
    if option == '1':
        van()
    elif option == '2':
        financial()


def financial():
    text_financial = bold + "One week has passed, and poor financial decisions have led to you losing all the money. \
    However, you still have the card." + reset_bold
    print(textwrap.fill(text=text_financial, width=80, replace_whitespace=False))
    print("Make a decision")
    print("1 - Throw out the card and find a new job")
    print("2 - Call the number and accept the offer.")
    option = input("Enter your choice: ")
    while not(option == '1' or option == '2'):
        option = input("Invalid Answer. Enter your choice again(1 or 2): ")
    if option == '1':
        homeless()
    elif option == '2':
        van()

def homeless():
    text_homeless = bold + "You Lose\nafter a couple days, you quickly realize that you have no chance of \
    getting a job with the poor living conditions you're in and live the rest of your life homeless " + reset_bold
    print(textwrap.fill(text=text_homeless, width=80, replace_whitespace=False))
    input("Press Enter to Restart: ")
    home()

def van():
    text_van = bold + "\nYou get picked up in a van and wake up in a facility with hundreds of other people. \
The people running the facility announces that there will be 6 games played over 6 days with a grand prize of 36 million USD." + reset_bold
    print(textwrap.fill(text=text_van, width=80, replace_whitespace=False))
    has_friends = False
    print("Make a decision")
    print("1 - Try to form an alliance ")
    print("2 - Sit alone and ignore others")
    option = input("Enter your choice: ")
    while not(option == '1' or option == '2'):
        option = input("Invalid Answer. Enter your choice again(1 or 2): ")
    if option == '1':
        has_friends = True
        first_game(has_friends)
    if option == '2':
        has_friends = False
        first_game(has_friends)

def first_game(has_friends):
    text_first_game = bold + "\nThe first game is announced and it is red light, green light. However, \
you have only 5 minutes to get across the line." + reset_bold
    print(textwrap.fill(text=text_first_game, width=80, replace_whitespace=False))
    print("Make a decision")
    print("1 - Take your time and watch your step ")
    print("2 - Stand behind people to hide movement and move at a comfortable pace.")
    print("3 - Run and try to get across quickly")
    option = input("Enter your choice: ")
    while not(option == '1' or option == '2' or option == '3'):
        option = input("Invalid Answer. Enter your choice again(1, 2, or 3): ")
    if option == '1':
        lose_slow()
    if option == '2':
        first_win(has_friends)
    if option == '3':
        lose_fast()

def lose_slow():
    text_lose_slow = bold + "\nYou Lose\nThe timer runs out you get shot after only making it past halfway." + reset_bold
    print(textwrap.fill(text=text_lose_slow, width=80, replace_whitespace=False))
    input("Press Enter to Restart")
    home()

def lose_fast():
    text_lose_fast = bold + "\nYou Lose\nYou run at a quick pace and almost make it to the finish line,\
however you trip and get shot." + reset_bold
    print(textwrap.fill(text=text_lose_fast, width=80, replace_whitespace=False))
    input("Press Enter to Restart")
    home()

def first_win(has_friends):
    text_first_win = bold + "\nYou barely get across with only 20 seconds left on the timer and\
 then head back to the main room " + reset_bold
    print(textwrap.fill(text=text_first_win, width=80, replace_whitespace=False))
    input("Press Enter to Continue")
    second_game(has_friends)


def second_game(has_friends):
    text_second_game = bold + "\nThe hosts have now brought everyone to play a new game in an indoor playground.\
In front of you, there are four shapes to choose from." + reset_bold
    print(textwrap.fill(text=text_second_game, width=80, replace_whitespace=False))
    print("1 - \u25B3")
    print("2 - \u2602")
    print("3 - \u2299")
    print("4 - \u2605")
    option = input("Choose a shape: ")
    while not(option == '1' or option == '2' or option == '3' or option == '4'):
        option = input("Invalid Answer. Enter your choice again(1, 2, 3, or 4): ")
    if option == '1':
        dalgona(True, has_friends)
    elif option == '2':
        dalgona(False, has_friends)
    elif option == '3':
        dalgona(True, has_friends)
    elif option == '4':
        dalgona(False, has_friends)

def dalgona(shape, has_friends):
    text_dalgona = bold + "\nThe game is now revealed as Dalgona. Players must carve out their \
 shape using a pin without any cracks within a 10 minute time frame." + reset_bold
    print(textwrap.fill(text=text_dalgona, width=80, replace_whitespace=False))
    print("1 - Carve it out slowly and carefully ")
    print("2 - Use a lighter you found on the floor")
    print("3 - Use your tongue and lick the cookie to melt the shape out")
    option = input("Choose a shape: ")
    while not(option == '1' or option == '2' or option == '3'):
        option = input("Invalid Answer. Enter your choice again(1, 2, or 3): ")
    if option == '1' and shape == True:
        win_1(has_friends)

    elif option == '2':

        win_2(has_friends)

    elif option == '3':
        win_3(has_friends)

    elif option == '1' and shape == False:
        lose_dalgona()

def lose_dalgona():
    text_lose_dalgona = bold + "\nYou Lose. The timer runs out and you are not even close to be finished,\
 and you must now suffer the consequences." + reset_bold
    print(textwrap.fill(text=text_lose_dalgona, width=80, replace_whitespace=False))
    input("Press Enter to Restart: ")
    home()

def win_1(has_friends):
    text_win_1 = bold + "\nCongratulations, you carved it out with over 3 minutes left." + reset_bold
    print(textwrap.fill(text=text_win_1, width=80, replace_whitespace=False))
    input("Press Enter to Continue: ")
    midnight_fight(has_friends)

def win_2(has_friends):
    text_win_2 = bold + "\nThe lighter really helped and you finished with over 5 minutes left." + reset_bold
    print(textwrap.fill(text=text_win_2, width=80, replace_whitespace=False))
    input("Press Enter to Continue: ")
    midnight_fight(has_friends)

def win_3(has_friends):
    text_win_3 = bold + "\nSeems like an odd technique, however it worked in the end and you survive." + reset_bold
    print(textwrap.fill(text=text_win_3, width=80, replace_whitespace=False))
    input("Press Enter to Continue: ")
    midnight_fight(has_friends)

def midnight_fight(has_friends):
    text_midnight_fight = bold + "\nAfter resting for a little bit, a fight breaks out and the guards are not preventing it.\
 You soon realize that a fight will break out and you must make a decision." + reset_bold
    print(textwrap.fill(text=text_midnight_fight, width=80, replace_whitespace=False))
    if has_friends == True:
        print("1 - Work with your team and look out for each other's backs to increase chances of survival.")
    print("2 - Go around and try to kill as many people as possible to increase the prize pool.")
    if has_friends == False:
        print("3 - Go around and ask people if they want to form an alliance.")
    option = input("Make a choice: ")
    while not(option == '1' or option == '2' or option == '3'):
        option = input("Invalid Answer. Enter your choice again(1, 2, or 3): ")
    if option == '1':
        third_game()
    if option == '2':
        midnight_die()
    if option == '3':
        midnight_die()

def midnight_die():
    text_midnight_die = bold + "\nYou get stabbed in the back and die from bleeding." + reset_bold
    print(textwrap.fill(text=text_midnight_die, width=80, replace_whitespace=False))
    input("Press Enter to Restart:")
    home()

def third_game():
    text_third_game = bold + "\nNext game is revealed as Tug of War. You will now be assigned a random team of 5.\n~~~~~~~~~~" + reset_bold
    print(textwrap.fill(text=text_third_game, width=80, replace_whitespace=False))
    strength = 0
    sleep(2)
    for i in range(5):
        print(random.choice(players))
    if random.choice(players) == 'young woman':
        strength += 2
    if random.choice(players) == 'old man':
        strength += 2
    if random.choice(players) == 'old woman':
        strength += 1
    if random.choice(players) == 'middle-aged man':
        strength += 3
    if random.choice(players) == 'middle-aged woman':
        strength += 1.5
    if random.choice(players) == 'intelligent man':
        strength += 4
    if random.choice(players) == 'body builder':
        strength += 5
    if random.choice(players) == 'teenager':
        strength += 1
    print(strength)


def fourth_game():
    pass

def fifth_game():
    pass

def sixth_game():
    pass
start()