alphabet = 'abcdefghijklmnopqrstuvwxyz'
s = input("Give me a string: ")

# test_string = The quick brown fox jumps over the lazy dog

lowered_string = s.lower()
error = 0

for i in range(0, len(alphabet)):
    if alphabet[i] not in s:
        error = 1
        break

if (error == 1):
    print("False")
else:
    print("True")

# OR
import string

s = "The quick brown fox jumps over the lazy dog"
    
set_s = set(s.lower())
set_s.remove(" ")
print(set_s == set(string.ascii_lowercase))

# OR 2

import string

s = "The quick brown fox jumps over the lazy dog"
is_pangram = True

for char in string.ascii_lowercase:
    if char not in s.lower():
        is_pangram = False

print(is_pangram)