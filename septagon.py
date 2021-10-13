def my_function(x):

    return list(dict.fromkeys(x))

mylist = my_function([1, 2, 5, 6, 9, 3, 2, 1, 5, 6])

print(mylist)