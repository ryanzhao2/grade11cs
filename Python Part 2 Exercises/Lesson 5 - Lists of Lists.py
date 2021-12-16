"""
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



#QUESTION #1
def print_books(list_of_books):

    for book in list_of_books:
        print(f' {book[0][0:30]:<30} by {book[1][0:20]:<20} {str(book[5]):<4} rated {str(book[2])[0:3]}')

#QUESTION #2
def print_detailed_book(list_of_books):
    format = '-'
    for book in list_of_books:
        print(f' {book[0]}\n'
              f' by: {book[1]}\n'
              f' {book[5]}\n'
              f' {format * len(book[0])}\n'
              f' ${book[4]:.2f}\n\n'
              f' {book[6]}\n'
              f' rated {book[2]}   for  {book[3]} reviews\n\n\n')





def main():
    main_book_list = generate_list_books("amazon_bestseller_books.csv")

    #print(main_book_list[:10])

    print_books(main_book_list)

    print_detailed_book(main_book_list)

main()
"""