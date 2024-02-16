s = input("Give me a string: ")

if len(s) < 6:
    print("")
else:
    print(s[0:3:] + s[len(s)-3::])