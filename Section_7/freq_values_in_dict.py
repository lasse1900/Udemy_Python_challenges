my_dict = {
	"a": 4,
	"b": 4,
	"c": 2,
	"d": 7,
	"e": 4,
	"f": 2,
	"g": 7,
	"h": 7
 }

freq_dict = {}

# my_values = set(my_dict.values())
# print(my_values)

# for i in my_dict:
#     if my_dict.values() == my_values:

for value in my_dict.values():
    if value in freq_dict:
        freq_dict[value] += 1
    else:
        freq_dict[value] = 1
print(freq_dict)