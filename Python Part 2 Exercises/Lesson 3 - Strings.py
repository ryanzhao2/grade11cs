#THURSDAY NOV 25 2021
#MR. SHAFT
#RYAN ZHAO
#QUESTION #1
"""
s1 = "spam"
s2 = "ni!"

print("The Knights who say, " + s2) #adding "ni" to this string
print("Hello\nWorld\n\nGoodbye \n") #printing 1 new line between Hello and World and then 2 new lines between World and Goodbye and then a new line after that
print(3 * s1 + 2 * s2) #Printing "spam" 3 times and then "ni!" 2 times
print(s1[1]) #Prints the second letter(index 1) of "spam" which is "p"
print(s1[1:3]) #Print the second letter(index 1) and third letter(index 2) of "spam" which is "pa"
print(s1[2] + s2[:2]) #Prints the third letter(index 2) of "spam" and also the first and second letters of "ni!" which is "ni" so it becomes "ani"
print(s1.upper()) #Prints "spam" in uppercase so its "SPAM"
print(f'{s2.upper() * 3:<4}') #Prints "ni!" in uppercase 3 times and lefts aligns it 4 characters
#Operators demonstrated are multiplication and addition

"""
#QUESTION #2
"""
word = "dinosaur"
print(word[0]) #PRINTS "d"
print(word[-1]) #PRINTS "r"
print(word[1:2]) #PRINTS "i"
print(word[1:4]) #PRINTS "ino"
print(word[-3:-1]) #PRINTS "au"
"""

#QUESTION #3
"""
wordG = "gorilla"
wordH = "hippopotamus"
wordJ = "jackal"

print(f'{wordG:>30}')
print(f'{wordH:^30}')
print(f'{wordJ:<30}')

wordG = "gorilla"
wordH = "hippopotamus"
wordJ = "jackal"

print(f'{wordG:<30}')
print(f'{wordH:>30}')
print(f'{wordJ:^30}')
"""

#QUESTION #4
"""
print("aardvark" < "apple")
print("Zebra" < "anteater")
print("horse" > "cart")
print("egg" < "chicken")

if "elephant" < "mouse":
    print("only alphabetically")
#CHECKS IF ONE WORD COMES BEFORE THE OTHER WORLD ALPHABETICALLY
"""

#QUESTION #5
"""
one = input("Please enter word 1:")
two = input("Please enter word 2:")
if one < two:
    print(f'Alphabetical Order: {one} {two}')

else:
    print(f'Alphabetical Order: {two} {one}')
"""

#QUESTION #6
"""
s = "the quick brown fox jumps over the lazy dog"

print(s.count("o")) #CHECKS HOW MANY TIMES THE LETTER "O" OCCURS
print(s.lower()) #CHANGES THE ENTIRE STRING TO LOWERCASE(does nothing because everything is already lowercase)
print(s.replace('fox', 'lamb')) #replaces the word "fox" with "lamb"
print(s.find('o')) #finds the index of the first occurence of the letter "o"
"""
#QUESTION #7
"""
user_input = input("Enter a number in the format 12,123: ")
print(user_input.replace(",", ""))
"""

#QUESTION #8
"""
word = input("Please enter a word")
word = word.title()
print (word)
check = word.istitle()
print (check)
#istitle() checks if each word starts with an uppercase letter and returns a boolean value
#title() returns a string where the first character in each word is uppercase
"""

#QUESTION #9
"""
word = "rabbit"
length = len(word)
#should print "bb"
if length % 2 == 0:
    print(word[length//2-1:length//2+1])
else:
    print(word[length//2:length//2+1])

word2 = "mouse"
length2 = len(word2)
#should print "u"
if length2 % 2 == 0:
    print(word2[length2//2-1:length2//2+1])
else:
    print(word2[length2//2:length2//2+1])
"""

#QUESTION #10
"""
def encode_word(some_word):
    length = len(some_word)
    if length % 2 == 0:
        even = some_word[length // 2 - 1:length // 2 + 1]
        print(some_word[0:length // 2-1] + some_word[length // 2 + 1:] + even)
    else:
        odd = some_word[length // 2:length // 2 + 1]
        print(some_word[0:length // 2] + some_word[length // 2 + 1:] + odd)

# MAIN
word = input("Enter a word")
encode_word(word)
"""

#QUESTION #11
"""
def spaced_word(some_word):
    space = ''
    for i in some_word:
        space += i + ' '

    print(space[:-1])


#MAIN
word = input("Enter a word: ")
spaced_word(word)
"""

#QUESTION #12
"""
def print_months():
    months = "JanFebMarAprMayJunJulAugSepOctNovDec"
    for i in range(0, 36, 3):
        print(f'{(i+3)//3:>3}. {months[i:i+3]}')

#MAIN
print_months()
"""

#QUESTION #13
"""
def reverse(some_string):

    text = ""
    for i in range(len(some_string)):
        text += some_string[len(some_string) - i - 1]
    return text


# MAIN
s = input("Enter a word or sentence")
print(reverse(s))

# SAMPLE RUN
# happy would change to yppah
# Hello World would change to dlroW olleH
"""

#QUESTION #14
"""
def count_vowels(some_string):
    count = 0
    for char in some_string:
        if char == 'i' or char == 'o' or char == 'e' or char == 'a' or char == 'u':
            count += 1
    return count



#MAIN
s = input("Enter some word or sentence")
answer = count_vowels(s)
print(f'There are {answer} vowels')
"""

#QUESTION #15
"""
def remove_letter(letter, some_string):
    empty_string = ""
    for i in some_string:
        if i != letter:
            empty_string += i

    return(empty_string)


print(remove_letter('i', 'Mississauga'))
"""
