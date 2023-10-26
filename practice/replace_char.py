
s = input('string: ')
curr_char = input('old char: ')
new_char = input('new char: ')
new_string = ''

for i in range(len(s)):
    if s[i] == curr_char:
        new_string = new_string + new_char
    else:
        new_string = new_string + s[i]

print(new_string)