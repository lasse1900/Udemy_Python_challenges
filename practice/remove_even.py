
s = input()

if len(s) <= 1:
    print(s)
else:
    for i in range(len(s)):
        if i % 2 != 0:
            print(s[i], end='')

