
string = input("Give a string - I'll change commas to dots: ")

word = 'Rati123kka'
new = ''
for char in word:
    if char.isalpha():
        char = char.swapcase()
        new += char

print(new)

