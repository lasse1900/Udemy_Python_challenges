s = input("Give me a string: ")

new_string = s.swapcase()

words = new_string.split(" ")
reversed_string = ""
for word in words:
    print(word[::-1], end = " ")
    reversed_string += word[::-1] + " "

print()
print("--------------")
print(reversed_string.rstrip())