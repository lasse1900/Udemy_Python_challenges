
given_s = input("Give a string - I'll remove spaces: ")
prefix = input("Give me the prefix: ")

output = 'False'

given_list = list(given_s)
prefix_list = list(prefix)

if prefix_list[::] == given_list[0:len(prefix_list)]:
    output = 'True'

print(output)


#-----------------

print(given_s[:len(prefix)] == prefix)