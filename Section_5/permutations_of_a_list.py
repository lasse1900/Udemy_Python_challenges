import itertools

my_list = [1,2,3]
permutations =  list(itertools.permutations(my_list))

for item in permutations:
    print(item)

