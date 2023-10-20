
given_s = input("Give a string - I'll remove spaces: ")
suffix = input("Give me the prefix: ")

output = 'False'

given_list = list(given_s) # Hello1
suffix_list = list(suffix) # lo1

print('suffix', suffix_list)
print('-'*20)
print('list',given_list[-len(suffix):])

if suffix == given_s[-len(suffix):]:
    output = 'True'

print(output)

#-----------------

print(given_s[-len(suffix):] == suffix)