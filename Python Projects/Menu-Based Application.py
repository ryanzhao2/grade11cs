import csv


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
    print("\n" * 5)
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
        choice = input("Type number to choose ...")

    return int(choice)


def get_all_possible_writers(list_of_movies):
    writers = []

    for movie in list_of_movies:
        for writer in movie[7]:
            if writer not in writers:
                writers.append(writer)

    writers.sort()
    return writers


def print_writers(list_writers):
    print("\n\nAll writers available are:")
    print("-" * 20)

    for item in list_writers:
        print(f'{item:<30}')

    print("\n")


def get_valid_writer(list_writers):
    writer = input("What writer would you like to filter for?")
    while writer not in list_writers:
        writer = input("Sorry that writer name is not valid. Please try again")

    return writer


def filter_all_listings(list_of_movies, writer):
    sub_list = []

    for item in list_of_movies:
        if writer in item[7]:
            sub_list.append(item)

    return sub_list


def get_valid_listing(list_movies):
    possible_choice_values = []
    for i in range(0, len(list_movies)):
        possible_choice_values.append(str(i + 1))

    choice = input("Which listing would you like to choose?")

    while choice not in (possible_choice_values):
        choice = input("Invalid choice. Try another number")

    choice = int(choice) - 1

    return list_movies[choice]


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


def main():
    main_movie_list = generate_list_movies("movie_data.csv")

    all_writers = get_all_possible_writers(main_movie_list)

    menu_items = ['See All Listings', 'Find movie by Writer', 'Quick and Smart Search', 'Favourites', 'TBD', 'Exit']

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
            pass

        elif choice == 4:
            pass

        elif choice == 5:
            pass

        print_menu(menu_items)
        choice = get_menu_selection(menu_items)

    print("\n\nGoodbye! Enjoy Playing.")


main()
