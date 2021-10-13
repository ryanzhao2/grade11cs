def shuffle(onelist, twolist):
    if len(onelist) >= 1 and len(twolist) >= 1:
        x = zip(onelist, twolist)
        return list(x)
    if len(onelist) == 0 and len(twolist) >= 1:
        return twolist
    elif len(twolist) == 0 and len(onelist) >= 1:
        return onelist
    else:
        return None



rList = (1, 3, 5)
yList = (2, 4, 6)

myList = shuffle(rList, yList)
myList2 = []
for i in myList:
    myList2.append(i[0])
    myList2.append(i[1])

print(myList2)