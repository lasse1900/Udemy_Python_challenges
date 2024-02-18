
new_key = input("Give new key: ")
new_value = input("Give new value: ")


my_dict = {"January": 45, "February": 56, "March": 67}

if new_key not in my_dict:
    my_dict[new_key] = new_value

print(my_dict)

