my_dict1 = {"a": 1, "b": 2, "c": 3}
my_dict2 = {"c": 4, "d": 6, "e": 8}

merged_dict = {**my_dict1, **my_dict2}
print(merged_dict)

merged = my_dict1 | my_dict2
print(merged)