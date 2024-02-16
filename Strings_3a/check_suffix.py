s = input("Give me a string: ")
my_suffix = input("Give the suffix: ")

if int(len(my_suffix)) >= len(s):
    print("False")
elif s.endswith(my_suffix):    
    print("True")
else:
    print("False")


# OR
    
print(s[-len(my_suffix):] == my_suffix)