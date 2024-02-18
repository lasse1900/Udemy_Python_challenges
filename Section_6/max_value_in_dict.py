my_dict1 = {"a": 4, "b": 3, "c": 7,"d":6}
# my_dict1 = {}

if len(my_dict1) == 0:
    print("Empty")

my_set = set(my_dict1.values())
print(max(sorted(my_set)))

