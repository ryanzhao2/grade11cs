import csv
import collections
bold = "\033[1m"
reset_bold = "\033[0m"


def generate_list_movies(filename):
    movie_list = []

    file_in = open(filename, encoding='UTF-8', errors='replace')

    file_in.readline()
    file_in = csv.reader(file_in)

    for line in file_in:
        line[2] = int(line[2])
        line[3] = line[3].split(";")
        line[5] = int(line[5])
        line[6] = line[6].split(";")
        line[7] = line[7].split(";")
        line[8] = int(line[8])
        line[9] = int(line[9])

        movie_list.append(line)

    return movie_list


def print_menu(menu_list):
    print("\n" * 3)
    for i in range(0, len(menu_list)):
        print(f'{i + 1}. {menu_list[i]}')


def get_menu_selection(menu_list):
    possible_choice_values = []
    for i in range(0, len(menu_list)):
        possible_choice_values.append(str(i + 1))

    choice = input("Type number to choose ... ")

    while choice not in possible_choice_values:
        print("Incorrect selection")
        print("\n" * 30)

        print_menu(menu_list)
        choice = input("Type number to choose ... ")

    return int(choice)


#~~~~~~~~~~STARTER CODE WRITER STUFF~~~~~~~~~~~~~~~~~


def filter_all_listings(list_of_movies, writer):
    sub_list = []

    for item in list_of_movies:
        if writer in item[7]:
            sub_list.append(item)

    return sub_list

def get_all_possible_writers(list_of_movies):
    writers = []

    for movie in list_of_movies:
        for writer in movie[7]:
            if writer not in writers:
                writers.append(writer)

    writers.sort()
    return writers

def get_valid_writer(list_writers):
    writer = input("What writer would you like to filter for? ")
    while writer not in list_writers:
        writer = input("Sorry that writer name is not valid. Please try again ")

    return writer

def get_valid_listing(list_movies):
    possible_choice_values = []
    for i in range(0, len(list_movies)):
        possible_choice_values.append(str(i + 1))

    choice = input("Which listing would you like to choose?")

    while choice not in (possible_choice_values):
        choice = input("Invalid choice. Try another number")

    choice = int(choice) - 1

    return list_movies[choice]

def print_writers(list_writers):
    print("\n\nAll writers available are:")
    print("-" * 20)
    for item in list_writers:
        print(f'{item:<30}')

    print("\n")


def print_listings_table(list_movies):
    for i in range(0, len(list_movies)):
        movie = list_movies[i]
        s = f'{i + 1:<3} {movie[1][:30]:<30}'
        print(s)


def print_movie_details(some_movie):
    s = "\n"
    s += f'{some_movie[1]} {some_movie[2]}\n'
    s += f'grossed ${some_movie[5]:,}\n'
    s += f'{some_movie[3]}\n'
    s += f'Rotten Tomato Score: {some_movie[9]}%\n\n'
    s += some_movie[11]

    print(s)

#~~~~~~~~~~~~~~~~~FEATURE #1~~~~~~~~~~~~~~~~~~~~~~~~~~

# smart search by title~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def smart_search_movie_list_by_title(main_movie_list):
    movie_list_by_title = []
    t = input('\nSearch by Title - Enter a full title or part of a title: ')
    found_title = False
    while found_title == False:
        for m in main_movie_list:
            if t.upper() in m[1].upper():
                movie_list_by_title.append(m)
        if len(movie_list_by_title) != 0:
            found_title = True
        else:
            t = input( 'Title not found, Enter a full title or part of a title: ')

    print(bold + '\nHere are the movies featured with the chosen title:' + reset_bold)
    return movie_list_by_title

# smart search by genre~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def smart_search_movie_list_by_genre(movie_list_by_title):
    movie_list_by_genre = []
    g = input('\nSearch by Genre - Enter a full genre or part of a genre: ')
    found_genre = False
    while found_genre == False:
        for m in movie_list_by_title:
            for i in range (len(m[3]) ):
                if g.upper() in m[3][i].upper():
                    movie_list_by_genre.append(m)
                    break
        if len(movie_list_by_genre) != 0:
            found_genre = True
        else:
            g = input('Genre not found, Enter a full genre or part of a genre: ')

    print(bold + '\nHere are the movies featured with the chosen genre:' + reset_bold)
    return movie_list_by_genre

# smart search by actor~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def smart_search_movie_list_by_actor(movie_list_by_genre):
    movie_list_by_actor = []
    a = input('\nSearch by Actor - Enter a full actor\'s name or part of an actor\'s name: ')
    found_actor = False
    while found_actor == False:
        for m in movie_list_by_genre:
            for i in range (len(m[6]) ):
                if a.upper() in m[6][i].upper():
                    movie_list_by_actor.append(m)
                    break
        if len(movie_list_by_actor) != 0:
            found_actor = True
        else:
            a = input('Actor not found, Enter a full actor\'s name or part of an actor\'s name: ')

    print(bold + '\nHere are the movies featured with the chosen actor:' + reset_bold)
    return movie_list_by_actor

# smart search by writer~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def smart_search_movie_list_by_writer(movie_list_by_actor):
    movie_list_by_writer = []
    w = input('\nSearch by Writer - Enter a full writer\'s name or part of a writer\'s name: ')
    found_writer = False
    while found_writer == False:
        for m in movie_list_by_actor:
            for i in range (len(m[7]) ):
                if w.upper() in m[7][i].upper():
                    movie_list_by_writer.append(m)
                    break
        if len(movie_list_by_writer) != 0:
            found_writer = True
        else:
            w = input('Writer not found, Enter a full writer\'s name or part of a writer\'s name: ')

    print(bold + '\nHere are the movies featured with the chosen writer:' + reset_bold)
    return movie_list_by_writer


#~~~~~~~~~~~~~TITLE FORMATTING STUFF~~~~~~~~~~~~~~~~~

def smart_print_listings_table(list_movies):
    for i in range(0, len(list_movies)):
        movie = list_movies[i]
        s = f'{i + 1:<3} {movie[1][:60]:<30}'
        print(s)

#~~~~~~~~~~~~~~~~FEATURE #2~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#get list of titles
def smart_get_all_possible_titles(list_of_title_movies):
    titles = []


    for a_title in list_of_title_movies:
        if a_title[1] not in titles:
                titles.append(a_title[1])


    titles.sort()
    return titles


def display_movies(movies):
    print(bold + "\n\nAll movies available are:" + reset_bold)
    print("-" * 20)

    for item in movies:
        print(f'{item:<30}')

    print("\n")

def check_choice(title_list):
    count = 0
    favourites_list = []
    print('1 - Add Movie to Favourites List')
    print('2 - Exit')
    menu_choice = input("What would you like to do? ")
    while not(menu_choice == '1' or menu_choice == '2'):
        menu_choice = input("What would you like to do? Enter 1, 2, or 3 ")
    if menu_choice == '1':
        while len(favourites_list) < 5:
            favourite_choice = input("Enter a movie to add to your favourites list(you can add up to 5 max). Type done if you are done adding movies. ")
            if favourite_choice == 'done' and len(favourites_list) > 0:
                break
            if favourite_choice in title_list:
                favourites_list.append(favourite_choice)
                print(f'You added {len(favourites_list)} movies, you have {5 - len(favourites_list)} movie selections remaining.\n')
            else:
                print('Try again(you need atleast 1 movie)\n')
        print(f'Your favourite movies are {favourites_list}')
        print('1 - Access List')
        print('2 - Exit')
        menu_choice = input("What would you like to do next? \n")
        while not (menu_choice == '1' or menu_choice == '2'):
            menu_choice = input("What would you like to do? Enter 1 or 2: ")
            print('\n')
        if menu_choice == '1':
            ordered_choice_list = ['','','','','','','']
            for elem in favourites_list:
                if elem not in ordered_choice_list and count < len(favourites_list):
                    print(bold + f'{elem}' + reset_bold)
                    order_choice = input("What place would you put this movie in(1 for first, 5 for last)")
                    while not (order_choice == '1' or order_choice == '2' or order_choice == '3' or order_choice == '4' or order_choice == '5'):
                        order_choice = input(f'Enter a number that is less than {len(favourites_list) + 1}')
                    while not (int(order_choice) < int(len(favourites_list) + 1)):
                        order_choice = input(f'Enter a number that is less than {len(favourites_list) + 1}')
                    if order_choice == '1':
                        ordered_choice_list.insert(0, elem)
                        count += 1
                    if order_choice == '2':
                        ordered_choice_list.insert(1, elem)
                        count += 1
                    if order_choice == '3':
                        ordered_choice_list.insert(2, elem)
                        count += 1
                    if order_choice == '4':
                        ordered_choice_list.insert(3, elem)
                        count += 1
                    if order_choice == '5':
                        ordered_choice_list.insert(4, elem)
                        count += 1

            print(bold + f'\nYour favourite movies are in order {ordered_choice_list}' + reset_bold)
        if menu_choice == '2':
            print('\n\nGoodbye, Thanks for visiting')
            return



    if menu_choice == '2':
        print('\n\nGoodbye, Thanks for visiting')
        return


#~~~~~~~~~~~~~~~~MAIN STUFF~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def main():

    main_movie_list = generate_list_movies("movie_data.csv")

    all_writers = get_all_possible_writers(main_movie_list)
    all_titles = smart_get_all_possible_titles(main_movie_list)

    menu_items = ['See All Listings', 'Find movie by Writer', 'Quick and Smart Search', 'Favourites', 'Exit']
    print_menu(menu_items)
    choice = get_menu_selection(menu_items)

    while 0 < choice and choice < len(menu_items):

        ##See all listings
        if choice == 1:
            print_listings_table(main_movie_list)

        # Find listing by Genre
        elif choice == 2:
            print_writers(all_writers)
            writer = get_valid_writer(all_writers)

            sub_list_writers = filter_all_listings(main_movie_list, writer)
            print_listings_table(sub_list_writers)

            current_movie = get_valid_listing(sub_list_writers)

            print_movie_details(current_movie)

        elif choice == 3:

            movie_list_by_title = smart_search_movie_list_by_title(main_movie_list)
            smart_print_listings_table(movie_list_by_title)
            #print(movie_list_by_title)
            movie_list_by_genre = smart_search_movie_list_by_genre(movie_list_by_title)
            smart_print_listings_table(movie_list_by_genre)

            movie_list_by_actor= smart_search_movie_list_by_actor(movie_list_by_genre)
            smart_print_listings_table(movie_list_by_actor)

            movie_list_by_writer = smart_search_movie_list_by_writer(movie_list_by_actor)
            smart_print_listings_table(movie_list_by_writer)

        elif choice == 4:
            display_movies(all_titles)
            check_choice(all_titles)
        print_menu(menu_items)
        choice = get_menu_selection(menu_items)

    print("\n\nGoodbye! Enjoy Playing.")

main()