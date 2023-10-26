
s = input()
new_string = ''

for i in range(len(s)):
    if s[i] == ',':
        new_string += '.'
    else:
        new_string += s[i]

print(new_string)

print(s.replace(',','.'))

