def box(a, b):
    name = input("Enter your name")

s = '*'*(len(name)+2) + '\n'
s += f'*{name}*\n'
s += '*'*(len(name)+2) + '\n'

print(s)