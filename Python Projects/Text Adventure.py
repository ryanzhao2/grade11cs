import sys
import textwrap
import random
import time
from time import sleep

fancy_line = "~" * 75
bold = "\033[1m"
reset_bold = "\033[0m"
text_length = 80
new_line = "\n" * 30
short_line = "\n" * 3
good_shape = True
players = ['young woman', 'middle-aged woman', 'old man', 'middle-aged man',\
           'body builder', 'teenager', 'middle-aged man', 'old lady', 'intelligent man', 'young woman']
coin = ['heads', 'tails']
even_marbles = [2, 4, 6, 8, 10]
odd_marbles = [1, 3, 5, 7, 9]
even_or_odd = ['even', 'odd']
player_number = ['player_1', 'player_2']
left_right = ['left', 'right']




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
        sleep(1 / 10000000000000000000000000)
"""
def start():
    slow_print(bold + "Welcome to Squid Game\n" + reset_bold, text_length)
    input("Press Enter to Continue: ")

    home()

def home():
    slow_print(bold + "\nYou recently lost your job and have a hard time living with the little money available,\
 and also owe people some money.\n" + reset_bold, text_length)
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
    slow_print(bold + "\nYou forgot to wake up early the day of the interview, and arrive an hour late and fail the interview.\n"\
               + reset_bold, text_length)
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
    slow_print(bold + "\nYou start making money, however get greedy and lose it all in the end.\n" + reset_bold, text_length)
    print("1 - Walk to the train station to go home")
    input("Press Enter to Continue: ")
    train_station()


def train_station():
    slow_print(bold + "\nYou arrive at the train station and someone offers you to play a game to win some money,\
 and eventually you make some money from the game. He then passes a card to you with a number\
 on it and tells you to call it to make a lot more money.\n" + reset_bold, text_length)
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
    slow_print(bold + "One week has passed, and poor financial decisions have led to you losing all the money. \
    However, you still have the card.\n" + reset_bold, text_length)
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
    slow_print(bold + "You Lose\nafter a couple days, you quickly realize that you have no chance of \
    getting a job with the poor living conditions you're in and live the rest of your life homeless\n" + reset_bold, text_length)
    input("Press Enter to Restart: ")
    home()

def van():
    slow_print(bold + "\nYou get picked up in a van and wake up in a facility with hundreds of other people. \
The people running the facility announces that there will be 6 games played over 6 days with a grand prize of 36 million USD.\n" + reset_bold, text_length)
    has_friends = False
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
    slow_print(bold + "\nThe first game is announced and it is red light, green light. However, \
you have only 5 minutes to get across the line.\n" + reset_bold, text_length)
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
    slow_print(bold + "\nYou Lose\nThe timer runs out you get shot after only making it past halfway.\n" + reset_bold, text_length)
    input("Press Enter to Restart")
    home()

def lose_fast():
    slow_print(bold + "\nYou Lose\nYou run at a quick pace and almost make it to the finish line,\
however you trip and get shot.\n" + reset_bold, text_length)
    input("Press Enter to Restart")
    home()

def first_win(has_friends):
    slow_print(bold + "\nYou barely get across with only 20 seconds left on the timer and\
 then head back to the main room\n" + reset_bold, text_length)
    input("Press Enter to Continue: ")
    second_game(has_friends)


def second_game(has_friends):
    slow_print(bold + "\nThe hosts have now brought everyone to play a new game in an indoor playground.\
 In front of you, there are four shapes to choose from.\n" + reset_bold, text_length)
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
    slow_print(bold + "\nThe game is now revealed as Dalgona. Players must carve out their\
 shape using a pin without any cracks within a 10 minute time frame.\n" + reset_bold, text_length)
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
    slow_print(bold + "\nYou Lose. The timer runs out and you are not even close to be finished,\
 and you must now suffer the consequences.\n" + reset_bold, text_length)

    input("Press Enter to Restart: ")
    home()

def win_1(has_friends):
    slow_print(bold + "\nCongratulations, you carved it out with over 3 minutes left.\n" + reset_bold, text_length)
    input("Press Enter to Continue: ")
    midnight_fight(has_friends)

def win_2(has_friends):
    slow_print(bold + "\nThe lighter really helped and you finished with over 5 minutes left.\n" + reset_bold, text_length)
    input("Press Enter to Continue: ")
    midnight_fight(has_friends)

def win_3(has_friends):
    slow_print(bold + "\nSeems like an odd technique, however it worked in the end and you survive.\n" + reset_bold, text_length)
    input("Press Enter to Continue: ")
    midnight_fight(has_friends)

def midnight_fight(has_friends):
    slow_print(bold + "\nAfter resting for a little bit, a fight breaks out and the guards are not preventing it.\
 You soon realize that a fight will break out and you must make a decision.\n" + reset_bold, text_length)
    if has_friends == True:
        print("1 - Work with your team and look out for each other's backs to increase chances of survival.")
    print("2 - Go around and try to kill as many people as possible to increase the prize pool.")
    if has_friends == False:
        print("3 - Go around and ask people if they want to form an alliance.")
    option = input("Make a choice: ")
    while not(option == '1' or option == '2' or option == '3'):
        option = input("Invalid Answer. Enter your choice again(1, 2, or 3): ")
    if option == '1':
        midnight_survive()
    if option == '2':
        midnight_die()
    if option == '3':
        midnight_die()

def midnight_die():
    slow_print(bold + "\nYou get stabbed in the back and die from bleeding.\n" + reset_bold, text_length)
    input("Press Enter to Restart:")
    home()

def midnight_survive():
    slow_print(bold + "\nWorking with your team allowed everyone to survive safely.\n" + reset_bold, text_length)
    input("Press Enter to Proceed to the 3rd Game:")
    third_game()

def third_game():
    slow_print(bold + f"\nNext game is revealed as Tug of War. You will now be assigned a random team of 5.\n{fancy_line}\n" + reset_bold, text_length)

    strength = 0
    opponents_strength = 0
    sleep(2)
    team_list = []
    opponents_team_list = []
    for i in range(5):
        team = random.choice(players)
        opponents_team = random.choice(players)
        team_list.append(team)
        opponents_team_list.append(opponents_team)


        if team == 'young woman':
            strength += 2

        elif team == 'old man':
            strength += 1.5

        elif team == 'old woman':
            strength += 1

        elif team == 'middle-aged man':
            strength += 3

        elif team == 'middle-aged woman':
            strength += 1.5

        elif team == 'intelligent man':
            strength += 4

        elif team == 'body builder':
            strength += 5

        elif team == 'teenager':
            strength += 1

        elif team == 'old lady':
            strength += 0.5

        elif opponents_team == 'young woman':
            opponents_strength += 2

        elif opponents_team == 'old man':
            opponents_strength += 1.5

        elif opponents_team == 'old woman':
            opponents_strength += 1

        elif opponents_team == 'middle-aged man':
            opponents_strength += 3

        elif opponents_team == 'middle-aged woman':
            opponents_strength += 1.5

        elif opponents_team == 'intelligent man':
            opponents_strength += 3.5

        elif opponents_team == 'body builder':
            opponents_strength += 4

        elif opponents_team == 'teenager':
            opponents_strength += 1

        elif opponents_team == 'old lady':
            opponents_strength += 0.5
    print(f'Your Team is: {team_list}\n')
    print(f'Your Opponents Team is: {opponents_team_list}\n\nMake a Choice: \n')

    print("1 - Use entirely brute force to try to win the game")
    print("2 - Create a plan that doesnt require more force in order to win")
    print("3 - Find a way to not play the game")
    option = input("Enter your decision: ")
    while not(option == '1' or option == '2' or option == '3'):
        option = input("Invalid Answer. Enter your choice again(1, 2, or 3): ")
    if option == '1' and strength > opponents_strength:
        win_tug_of_war()
    elif option == '2' and 'intelligent man' in team_list and 'intelligent man' not in opponents_team_list:
        win_tug_of_war()
    elif option == '3':
        lose_tug_of_war()
    elif option == '2' and 'intelligent man' in team_list and 'intelligent man' in opponents_team_list:
        flip_coin()
    elif option == '1' and strength == opponents_strength:
        flip_coin()
    elif option == '2' and 'intelligent man' not in team_list and 'intelligent man' not in opponents_team_list:
        flip_coin()
    else:
        lose_tug_of_war()



def win_tug_of_war():
    slow_print(bold + "You win tug of war with a better team. Congratulations, you get to move on to the fourth game\n" + reset_bold, text_length)
    input("Press Enter to get a good nights sleep: ")
    fourth_game()

def lose_tug_of_war():
    slow_print(bold + "Bad team or bad choice, either one you still lose.\n" + reset_bold,text_length)

def flip_coin():
    slow_print(bold + "Looks like the teams have equal intelligence, flip a coin to determine your fate. Heads you win, tails you lose\n" + reset_bold, text_length)
    heads_tails = random.choice(coin)
    if heads_tails == 'heads':
        print("You got heads")
        win_tug_of_war()
    else:
        print("You got tails, unfortunate")
        lose_tug_of_war()

def fourth_game():
    slow_print(bold + "After the 3rd game, there are only 40 players remaining. The game hosts now reveal to you that the 4th game is marbles.\n\n\
Here are the Rules of the game\n" + reset_bold, text_length)
    slow_print("You and your opponent start off with 10 marbles each. One player chooses a number of marbles and places it in their fist infront of their opponent.\
 The opponent then guesses if the number of marbles in their hand is even or odd. If they are correct the player must give those marbles to the opponent and if they are wrong,\
 the opponent must give the player the number of marbles in their hand. The players switch turns after each play with the game ending when one player has all the marbles.", text_length)
    input("\n\nPress enter when you understand the rules: ")

    fourth_start()

def fourth_start():
    player_set = random.choice(player_number)
    print(f'\nYou are {player_set}')
    marbles = 10
    while marbles < 20 and marbles > 0:
        marble_even_odd_choice = random.choice(even_or_odd)
        total_marble_choice = random.randint(1, 20 - marbles)
        if player_set == 'player_1' and marbles > 0 and marbles < 20:

            choice = int(input("Choose a number of marbles: "))
            while(choice > (20 - marbles) and marbles >= 10  or choice == 0 and marbles >= 10):
                print(f'Choose a number within {20 - marbles} marbles that is 1 or higher')
                choice = int(input("Choose a number of marbles: "))
            while(choice > (20 - marbles) and marbles < 10 or choice == 0 and marbles < 10):
                print(f'Choose a number within {marbles} marbles that is 1 or higher')
                choice = int(input("Choose a number of marbles: "))
            player_set = 'player_2'
            if marble_even_odd_choice == 'even' and choice % 2 == 0 and choice <= marbles and choice >= 1:
                print(bold + f'Your opponent chose: {marble_even_odd_choice}\nYou lose {choice} marbles\
 and now have {marbles - choice} marbles left\n' + reset_bold)
                marbles -= choice

            elif marble_even_odd_choice == 'odd' and choice % 2 == 1 and choice <= marbles and choice >= 1:
                print(bold + f'Your opponent chose: {marble_even_odd_choice}\nYou lose {choice} marbles\
 and now have {marbles - choice} marbles left\n' + reset_bold)
                marbles -= choice

            else:
                print(bold + f'Your opponent chose: {marble_even_odd_choice}\nYou win {choice} marbles\
 and now have {marbles + choice} marbles \n' + reset_bold)
                marbles += choice

        if player_set == 'player_2' and marbles > 0 and marbles < 20:
            choose_even_or_odd = str(input("\nChoose an even or odd number of marbles: "))
            while not (choose_even_or_odd == 'even' or choose_even_or_odd == 'odd'):
                choose_even_or_odd = str(input("Invalid Answer. Enter your choice again(even or odd): "))
            player_set = 'player_1'
            if total_marble_choice % 2 == 0 and choose_even_or_odd == 'even':
                print(bold + f'Your opponent had {total_marble_choice} marbles, you won {total_marble_choice} marbles\
 and now have {total_marble_choice + marbles} marbles\n' + reset_bold)
                marbles += total_marble_choice

            elif total_marble_choice % 2 == 1 and choose_even_or_odd == 'odd':
                print(bold + f'Your opponent had {total_marble_choice} marbles, you won {total_marble_choice} marbles\
 and now have {total_marble_choice + marbles} marbles\n' + reset_bold)
                marbles += total_marble_choice

            else:
                print(bold + f'Your opponent had {total_marble_choice} marbles, you lost {total_marble_choice} marbles\
 and now have {marbles - total_marble_choice} marbles\n' + reset_bold)
                marbles -= total_marble_choice

    if marbles == 0:
        marble_loss()

    if marbles == 20:
        marble_win()

def marble_loss():
    slow_print(bold + "Unfortunately, you lost after having 0 marbles in your hand and now you must be punished\n" + reset_bold, text_length)
    home()

def marble_win():
    slow_print(bold + "Congratulations, you won marbles and now are able to advance to the fifth game\n" + reset_bold, text_length)
    input("Press Enter to Continue: ")
    fifth_game()
"""

def fifth_game():
    slow_print(bold + "Welcome to the fifth game contestants. You will be playing a game that involves choosing the right place to step.\
 There is tempered glass and normal glass. The tempered glass can hold 1 person. The normal glass cannot. You will be given the option to\
 choose either left or right. Make it to the end within the 25s time limit or you lose.\n" + reset_bold, text_length)
    count_win = 0
    start = time.time()
    for i in range(5):

        random_direction = 'right'
        choice = input("Choose left or right: ").lower()
        while not(choice == 'left' or choice == 'right'):
            print(f'Choose either left or right: ')
            choice = input("Choose left or right: ").lower()
        end = time.time()
        if end - start >= 25:
            print('timeout')
            home()
            break
        if choice == random_direction and (end - start < 25):
            print('keep going\n')
            count_win += 1
        else:
            print('You lost and unfortunately fall to your death.')
            home()
            break
    if count_win == 5:
        print('You win and now can move on to the final game.')
        sixth_game_rules()

def sixth_game_rules():
    slow_print(bold + "Wow, after 5 days of games, you managed to survive and now have arrived at the final game with one other opponent.\
 For this game, you will be playing squid game. Both players will have a steak knife. You will be playing as the attacker.\
 As the attacker, your goal is to go through the defender and touch the squids head with your foot. You will start off hopping\
 on one foot, however if you cut through the body of the squid, you can get back on two feet. If you get pushed out of bounds,\
 you lose. If you cannot continue, you lose. \n" + reset_bold, text_length)
    input("Press enter if you understand: ")
    sixth_game_part_1()

def sixth_game_part_1():
    print("Make a choice \n")
    print("1 - Go in towards the defender and aim for the eyes.\n")
    print("2 - Throw your knife at him and aim for the heart.\n")
    option = input("Enter your choice: ")
    print('\n')

    while not (option == '1' or option == '2'):
        option = input("Invalid Answer. Enter your choice again(1 or 2): ")
    if option == '1':
        sixth_game_part_2()
    elif option == '2':
        slow_print(bold + "The knife throw is uneffective and after receiving a minor cut, he now has two knives and you have none.\
 He then stabs you with both, leaving you with no options. You made it so far, however this is as far as you go." + reset_bold, text_length)
        home()

def sixth_game_part_2():
    print("That was good, your opponent now has trouble seeing with one eye, however he stabs you in the stomach.")
    print("1 - Leave the knife in your stomach and aim for the head.\n")
    print("2 - Take the knife out and use both knives to attack him.\n")
    option = input("Enter your choice: ")
    print('\n')

    while not (option == '1' or option == '2'):
        option = input("Invalid Answer. Enter your choice again(1 or 2): ")
    if option == '1':
        sixth_game_part_3()
    elif option == '2':
        slow_print(bold + "As soon as you take the knife out, you feel immense pain and your attacks now become very weak. He counter\
 attacks with a hard hit to your throat and then throws you out of the arena. You made it so far, however this is as far as you go." + reset_bold, text_length)
        home()

def sixth_game_part_3():
    print("It was a smart move, however he quickly reacts and blocks the attack and the knife falls out of your hand.")
    print("1 - Kick his ribs\n")
    print("2 - Quickly attack his other eye that is not injured\n")
    option = input("Enter your choice: ")
    print('\n')

    while not (option == '1' or option == '2'):
        option = input("Invalid Answer. Enter your choice again(1 or 2): ")
    if option == '1':
        slow_print(bold + "He takes the kick and is in pain, however he uses the rest of his strength to swing wide and hit the side of your skull.\
 You fall down and cannot continue. The guards then shoot you. You made it so far, however this is as far as you go." + reset_bold, text_length)
        home()
    elif option == '2':
        slow_print(bold + "He now can hardly see. You take advantage of this and finish him off with continuous blows to the head. After defeating him you\
 step on the squids head and win the game.\n\n" + reset_bold, text_length)
        win_squid_game()

def win_squid_game():
    slow_print(bold + "Congratulations! After going through 6 of our games, you rise on top and is last one standing.\
 Now that you won around 36 million dollars, you can live comfortably for the rest of your life." + reset_bold, text_length)

fifth_game()

