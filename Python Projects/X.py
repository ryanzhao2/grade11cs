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
#~~~~~~~~~~~~~~~~~TITLE STUFF~~~~~~~~~~~~~~~~~

def smart_get_all_possible_titles(list_of_title_movies):
    titles = []


    for a_title in list_of_title_movies:
        if a_title[1] not in titles:
                titles.append(a_title[1])


    titles.sort()
    return titles


def smart_get_title_search(titles_of_movie):
    found_title = False
    while found_title != True:
        title_input = input("\nEnter a partial title or full title: ")
        for title in titles_of_movie:
            if title_input.upper() in title.upper():
                found_title = True
                return title_input


def smart_filter_all_titles(list_of_title_movies, search_title):
    title_list = []


    for item in list_of_title_movies:

        if search_title.upper() in item.upper():
            title_list.append(item)

    return title_list

def print_listings_table(list_movies):
    for i in range(0, len(list_movies)):
        movie = list_movies[i]
        s = f'{i + 1:<3} {movie[1][:30]:<30}'
        print(s)


def smart_print_titles(movies):
    print(bold + "\n\nAll movies available are:" + reset_bold)
    print("-" * 20)

    for item in movies:
        print(f'{item:<30}')

    print("\n")

def smart_print_titles_table(list_titles):
    print('\n')
    print(bold + 'Here are the movies featured with the chosen title: ' + reset_bold)
    for i in range(0, len(list_titles)):
        movie = list_titles[i]
        s = f'{i + 1:<3} {movie[:][:30]:<30}'
        print(movie)

#~~~~~~~~~~~~~GENRE STUFF~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def smart_filter_all_genres2(main_list_of_movies, search_title, genre):
    genre_list = []

    for item in main_list_of_movies:
        if search_title.upper() in item[1].upper():
            for find_genre in item[3]:
                if genre.upper() in find_genre.upper():
                    genre_list.append(item)


    return genre_list

def smart_filter_all_genres(list_of_genre_movies, search_genre):
    sub_list = []

    for item in list_of_genre_movies:
        if search_genre in item[3]:
            sub_list.append(item[3])

    return sub_list


def smart_get_all_possible_genres(list_of_genre_movies):
    genres = []

    for a_genre in list_of_genre_movies:
        for search_genre in a_genre[3]:
            if search_genre not in genres:
                genres.append(search_genre)
    genres.sort()
    return genres


def smart_get_genre_search(genres_of_movies):
    found_genre = False
    while found_genre != True:
        genre_input = input(bold + "\nEnter a partial genre or full genre: " + reset_bold)
        for genre in genres_of_movies:
            if genre_input.upper() in genre.upper():

                found_genre = True
                return genre_input



def get_title_from_genre(get_genre, user_genre):
    print('\n')
    print(bold + f'Here are the movies featured with the chosen genre: {user_genre}**:' + reset_bold)
    for i in range(0, len(get_genre)):
        print(get_genre[i][1])

#~~~~~~~~~~~~~ACTOR STUFF~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def smart_filter_all_actors2(main_list_of_movies, search_title, genre, actors):
    actors_list = []

    for item in main_list_of_movies:
        if search_title.upper() in item[1].upper():
            for find_genre in item[3]:
                if genre.upper() in find_genre.upper():
                    for an_actor in item[6]:
                        if actors.upper() in an_actor.upper():
                            actors_list.append(item)


    return actors_list


def smart_get_actors_search(actors_of_movies):
    found_genre = False
    while found_genre != True:
        genre_input = input(bold + "\nEnter a partial actors name or full name: " + reset_bold)
        for genre in actors_of_movies:
            if genre_input.upper() in genre.upper():
                found_genre = True
                return genre_input

def smart_get_all_possible_actors(list_of_actor_movies):
    actors = []

    for an_actor in list_of_actor_movies:
        for search_actor in an_actor[6]:
            if search_actor not in actors:
                actors.append(search_actor)
    actors.sort()
    return actors

def smart_filter_all_actors(list_of_actor_movies, search_actor):
    sub_list = []

    for item in list_of_actor_movies:
        if search_actor in item[6]:
            sub_list.append(item[6])

    return sub_list

def get_title_from_actor(get_actor):
    print('\n')
    print(bold + 'Here are the movies featured with the chosen actor(s): ' + reset_bold)
    for i in range(0, len(get_actor)):
        print(get_actor[i][1])

#~~~~~~~~~~WRITER STUFF FOR PARTIAL AND SMART SEARCH~~~~~~~~


def smart_filter_all_writers2(main_list_of_movies, search_title, genre, actors, writers):
    writers_list = []

    for item in main_list_of_movies:
        if search_title.upper() in item[1].upper():
            for find_genre in item[3]:
                if genre.upper() in find_genre.upper():
                    for an_actor in item[6]:
                        if actors.upper() in an_actor.upper():
                            for a_writer in item[7]:
                                if writers.upper() in a_writer.upper():
                                    writers_list.append(item)

    return writers_list


def smart_get_writers_search(writers_of_movies):
    found_writer = False
    while found_writer != True:
        writer_input = input(bold + "\nEnter a partial writers name or full name: " + reset_bold)
        for writer in writers_of_movies:
            if writer_input.upper() in writer.upper():
                found_writer = True
                return writer_input

def smart_get_all_possible_writers(list_of_writers_movies):
    writers = []

    for an_actor in list_of_writers_movies:
        for search_writer in an_actor[7]:
            if search_writer not in writers:
                writers.append(search_writer)
    writers.sort()
    return writers

def smart_filter_all_writers(list_of_writer_movies, search_writer):
    sub_list = []

    for item in list_of_writer_movies:
        if search_writer in item[7]:
            sub_list.append(item[7])

    return sub_list

def get_title_from_writer(get_writer):
    print('\n')
    print(bold + 'Here are the movies featured with the chosen writer(s): ' + reset_bold)
    for i in range(0, len(get_writer)):
        print(get_writer[i][1])


#~~~~~~~~~~~~~~~~FEATURE #2~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def display_movies(movies):
    print(bold + "\n\nAll movies available are:" + reset_bold)
    print("-" * 20)

    for item in movies:
        print(f'{item:<30}')

    print("\n")

def check_choice(title_list):
    favourites_list = []
    print('1 - Add Movie to Favourites List')
    print('2 - Finish')
    print('3 - Access List')
    print('4 - Exit')
    user_choice = input("What would you like to do? ")
    while not(user_choice == '1' or user_choice == '2' or user_choice == '3' or user_choice == '4'):
        user_choice = input("What would you like to do? Enter 1, 2, 3, or 4 ")

    if user_choice == '1':
        user_choice_favourite = input("Enter a movie title to add to your favourites list:")
        if user_choice_favourite in title_list:
            favourites_list.append(user_choice_favourite)
            print('Movie has been added to favourites list')
            print('1 - Add Movie to Favourites List')
            print('2 - Finish')
            print('3 - Access List')
            print('4 - Exit')
            user_choice = input("What would you like to do? ")
        else:
            user_choice_favourite = input("Enter a movie title to add to your favourites list:")

    if user_choice == '2':
        print('1 - Add Movie to Favourites List')
        print('2 - Finish')
        print('3 - Access List')
        print('4 - Exit')
        user_choice = input("What would you like to do? ")
    if user_choice == '3':
        print('Your favourites list includes:', favourites_list)
        print('1 - Add Movie to Favourites List')
        print('3 - Exit')
        print('5 - Sort list from most favourite to least favourite')
        user_choice = input("What would you like to do? ")
        while not (user_choice == '1' or user_choice == '3' or user_choice == '5'):
            user_choice = input("What would you like to do? Enter 1, 3, 5")

    if user_choice == '4':
        return



#~~~~~~~~~~~~~~~~MAIN STUFF~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def main():

    main_movie_list = generate_list_movies("movie_data.csv")

    all_writers = get_all_possible_writers(main_movie_list)
    all_titles = smart_get_all_possible_titles(main_movie_list)
    all_genres = smart_get_all_possible_genres(main_movie_list)
    all_actors = smart_get_all_possible_actors(main_movie_list)
    smart_all_writers = smart_get_all_possible_writers(main_movie_list)

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
            smart_print_titles(all_titles)
            title = smart_get_title_search(all_titles)

            sub_list_titles = smart_filter_all_titles(all_titles, title)

            smart_print_titles_table(sub_list_titles)

            genre = smart_get_genre_search(all_genres)
            print('#############', genre)
            getting_genre = smart_filter_all_genres2(main_movie_list, title, genre)
            get_title_from_genre(getting_genre, genre)

            actors = smart_get_actors_search(all_actors)
            getting_actors = smart_filter_all_actors2(main_movie_list, title, genre, actors)
            get_title_from_actor(getting_actors)

            writers = smart_get_writers_search(smart_all_writers)
            getting_writers = smart_filter_all_writers2(main_movie_list, title, genre, actors, writers)
            get_title_from_writer(getting_writers)

        elif choice == 4:
            display_movies(all_titles)
            check_choice(all_titles)
        print_menu(menu_items)
        choice = get_menu_selection(menu_items)

    print("\n\nGoodbye! Enjoy Playing.")


main()