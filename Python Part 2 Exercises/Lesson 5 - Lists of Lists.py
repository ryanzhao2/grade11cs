
def generate_list_books(filename):

    book_list = []

    file_in = open(filename, encoding='utf-8', errors='replace')

    file_in.readline()

    for line in file_in:
        line = line.strip().split(",")
        line[2] = float(line[2])
        line[3] = int(line[3])
        line[4] = int(line[4])
        line[5] = int(line[5])

        book_list.append(line)

    return book_list

def print_books(list_of_books):
    pass
    #for book in list_of_books:



def print_detailed_book(list_of_books):

    pass




def main():
    main_book_list = generate_list_books("amazon_bestseller_books.csv")

    #print(main_book_list[:10])

    print_books(main_book_list)

    print_detailed_book(main_book_list)



main()
