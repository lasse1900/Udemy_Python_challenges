s = input("Give me a string: ")
index = int (input("Give me the index of the char you want to get: "))

if s == "":
    print("Empty String")
elif index > len(s)-1:
    print("i out of range")
else:
    print(s[index])

