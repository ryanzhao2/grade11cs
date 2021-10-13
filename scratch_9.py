import random
"""
title = "Random Number Generator"
print(title)
print("_" * len(title))
low = int(input("Enter a low value:"))
high = int(input("Enter a high value: "))
rando = (random.randrange(low, high, 10))

print(f'Your number is: {rando}')
"""
randos = []
for i in range(3):
    randos.append(random.randrange(1000,1050,50))
    print(f"Random Number #{i+1}: {randos[i]}")
    print(randos)