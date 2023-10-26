
s = input()

if len(s) < 6:
    print('')
else:
    print(s[0:3:1], end='')
    print(s[len(s)-3::1], end='')



