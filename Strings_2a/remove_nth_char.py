s = input("Give me a string: ")
nth = int(input("Remove char at index (give an integer): "))

new_string = ""
if (nth <= len(s) and (len(s) > 0)):
    new_string = s.replace(s[nth],"",1)
print(new_string)

# OR

if (len(s) == 0) or (nth >= len(s)):
    print(s)
else:
    new_s = ""
    for i in range(len(s)):
        if i != nth:
            new_s += s[i]
    print(new_s)
