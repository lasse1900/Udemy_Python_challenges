key = input("Please give a dictionary key, I'll inform if it can be found: ")

dict = {
    "a":4,
    "b":6
}

# dict = {}
# print(dict)

if key in dict.keys():
    print("True")
else:
    print("False")