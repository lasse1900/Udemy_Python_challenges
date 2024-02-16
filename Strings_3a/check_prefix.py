s = input("Give me a string: ")
my_prefix = input("Give the prefix: ")

if s.startswith(my_prefix):    
    print("True")
else:
    print("False")

# OR
    
print(s[:len(my_prefix)] == my_prefix)