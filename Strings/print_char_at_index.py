
string = input("Give a string: ")
print(string, '\n')
char_index = input("Give the index of chat in the string you want to get: ")

if int(len(string)) == 0:
    print('Empty String')
elif int(char_index) < len(string):
    print(string[int(char_index)])    
else:
    print('i is out of range')    

