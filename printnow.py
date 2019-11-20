counter = 0
sum = 0
for i in range(0,20,5):
    sum = sum + i
    counter = counter + 1
    print(i)
print("the sum is:",sum)
print("the average is:",sum / counter)
print(counter)