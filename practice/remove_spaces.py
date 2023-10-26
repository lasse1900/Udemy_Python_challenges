
s = input()
s2 = ''

print(s.replace(' ', ''))


for i in range(len(s)):
    if s[i] != ' ':
        s2 += s[i]

print(s2)

