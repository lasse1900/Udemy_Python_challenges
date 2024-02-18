
dict = {"a":4, "b":4, "c":4}
dict = {}

my_set = set(dict.values())
if len(my_set) == 0:
    print("Empty")
elif len(my_set) == 1:
    print("True")
else:
    print("False")
