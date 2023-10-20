
given_s = input("Give a string - I'll check if all alphabets (26) are present: ")
s = 'abcdefghijklmnopqrstuvwxyz'
alpha_s = s.lower()

myset = {''}
myset.clear()
myset.add(alpha_s)
output = 'True'
for char in alpha_s:
    if char == ' ':
        pass
    if char in given_s:
        pass
    else:
        output = 'False'
        break

print(output)

print('-'*20)
#---------------------------
out = 'True'
set_my = set(given_s.lower())
for char in set_my:
    if char == " ":
        pass
    elif char not in set_my:
        out = 'False'

print(out)
print("set_my: ", set_my)
print('-'*20)

# ---------------------
# Option 2
# ---------------------
import string

s = "The quick brown fox jumps over the lazy dog"
is_pangram = True

for char in string.ascii_lowercase:
    if char not in s.lower():
        is_pangram = False

print(is_pangram)

# ---------------------
# Option 3
# ---------------------
import string

s = "The quick brown fox jumps over the lazy dog"
is_pangram = True

for char in string.ascii_lowercase:
    if char not in s.lower():
        is_pangram = False
        break # Stop the loop immediately

print(is_pangram)

