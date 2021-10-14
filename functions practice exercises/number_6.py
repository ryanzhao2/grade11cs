def boxname(name):
    s = '*' * (len(name) + 2) + '\n'
    s += f'*{name}*\n'
    s += '*' * (len(name) + 2) + '\n'
    return s

name = input("Enter your name")


print(boxname(name))