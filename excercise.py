stringsada = "hello"
for i in range(len(stringsada)):
    if stringsada[i:i+1] not in "aeiou":
        print(stringsada[i:i+1]*2, end="")
    else:
        print(stringsada[i:i+1], end="")