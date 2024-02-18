# s1 = input("Give me another string of integers (comma separated): ")
# my_list = s1.split(',')
# print(my_list)

my_list = [1, 2, 3, 4]

def find_sum(s):
    if len(s) == 0:
        return 0
    else:
        return s[0] + find_sum(s[1:]) 
    
print(find_sum(my_list))